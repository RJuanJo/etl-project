import pandas as pd
import logging
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey
import json
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

def merge_data(**kwargs):
    logger = logging.getLogger(__name__)
    logger.info('Starting merge of transformed data')

    ti = kwargs['ti']
    api_data_json = ti.xcom_pull(task_ids='transform_api_task', key='api_data')
    data_etl_json = ti.xcom_pull(task_ids='transform_data_task', key='data_etl')

    api_data = pd.read_json(api_data_json)
    data_etl = pd.read_json(data_etl_json)

    try:
        merged_df = pd.concat([api_data, data_etl], ignore_index=True)
        merged_df['name'] = merged_df['name'].fillna('Unknown')
        merged_df['roomType'] = merged_df['roomType'].fillna('Unknown')
        merged_df['stars'] = merged_df['stars'].fillna(-999)

        for column in ['month', 'host_type']:
            mode_value = merged_df[column].mode()[0]
            merged_df[column] = merged_df[column].fillna(mode_value)

        for column in ['hot_tub', 'pool', 'bedrooms', 'bathrooms', 'revenue', 'occupancy', 'lead_time', 'length_stay', 'nightly_rate']:
            median_value = merged_df[column].median()
            merged_df[column] = merged_df[column].fillna(median_value)

        logger.info(f'Merged DataFrame shape: {merged_df.shape}')
        logger.info(f'Merged DataFrame preview:\n{merged_df.head()}')
        logger.info(f'Merged DataFrame preview:\n{merged_df.info()}')

        merged_df_json = merged_df.to_json(orient='records')
        ti.xcom_push(key='merged_data', value=merged_df_json)

        logger.info('Data merge complete')
    except Exception as e:
        logger.error('Failed during merging of data', exc_info=True)
        raise


def create_database():
    logger = logging.getLogger(__name__)
    logger.info('Creating database')

    try:
        with open('/config/credentials.json', 'r') as json_file:
            keys = json.load(json_file)
            host = keys["host"]
            user = keys["user"]
            password = keys["password"]
            database = keys["database"]
            port = keys["port"]

        default_engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}')
        
        with default_engine.connect() as conn:
            conn.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

        logger.info('Database created successfully')

    except Exception as e:
        logger.error('Failed to create database', exc_info=True)
        raise


def load_data(**kwargs):
    logger = logging.getLogger(__name__)
    logger.info('Starting to load data into the database')

    try:
        with open('/config/credentials.json', 'r') as json_file:
            keys = json.load(json_file)
            host = keys["host"]
            database = keys["database"]
            user = keys["user"]
            password = keys["password"]

        merged_data_json = kwargs['ti'].xcom_pull(task_ids='merge_data_task', key='merged_data')
        merged_df = pd.read_json(merged_data_json)
        
        engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

        with engine.connect() as conn:
            localization_df = merged_df[['city']].drop_duplicates().reset_index(drop=True)
            localization_df['localization_id'] = range(1, len(localization_df) + 1)
            localization_df.to_sql(name='DimLocalization', con=conn, if_exists='append', index=False)

            characteristics_df = merged_df[['stars', 'name', 'guests', 'openness', 'hot_tub', 'pool', 'bedrooms', 'bathrooms', 'occupancy', 'length_stay', 'revenue']].drop_duplicates().reset_index(drop=True)
            characteristics_df['characteristics_id'] = range(1, len(characteristics_df) + 1)
            characteristics_df.to_sql(name='DimCharacteristics', con=conn, if_exists='append', index=False)

            room_host_df = merged_df[['roomType', 'host_type']].drop_duplicates().reset_index(drop=True)
            room_host_df['room_host_id'] = range(1, len(room_host_df) + 1)
            room_host_df.to_sql(name='DimRoomHost', con=conn, if_exists='append', index=False)

            time_price_df = merged_df[['month', 'nightly_rate']].drop_duplicates().reset_index(drop=True)
            time_price_df['time_price_id'] = range(1, len(time_price_df) + 1)
            time_price_df.to_sql(name='DimTimePrice', con=conn, if_exists='append', index=False)

            fact_booking_df = pd.merge(merged_df, localization_df, on='city')
            fact_booking_df = pd.merge(fact_booking_df, characteristics_df, on=['stars', 'name', 'guests', 'openness', 'hot_tub', 'pool', 'bedrooms', 'bathrooms', 'occupancy', 'length_stay', 'revenue'])
            fact_booking_df = pd.merge(fact_booking_df, room_host_df, on=['roomType', 'host_type'])
            fact_booking_df = pd.merge(fact_booking_df, time_price_df, on=['month', 'nightly_rate'])

            fact_booking_df['booking_id'] = range(1, len(fact_booking_df) + 1)
            fact_booking_df = fact_booking_df[['booking_id', 'localization_id', 'characteristics_id', 'room_host_id', 'time_price_id', 'lead_time']]
            fact_booking_df.to_sql(name='FactBooking', con=conn, if_exists='append', index=False)

        logger.info('Data loaded into the database successfully')

    except SQLAlchemyError as e:
        logger.error('Failed to load data into the database', exc_info=True)
        raise
    except Exception as e:
        logger.error('Unexpected error', exc_info=True)
        raise