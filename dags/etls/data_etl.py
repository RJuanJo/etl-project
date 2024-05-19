import pandas as pd
import os
import logging
import numpy as np


def extract_data_etl(**kwargs):
    logger = logging.getLogger(__name__)
    logger.info('Starting data extraction for data_etl task')

    try:
        # Leer datos desde los CSVs
        amenities_df = pd.read_csv('/data/amenities.csv')
        market_analysis_df = pd.read_csv('/data/market_analysis_2019.csv')

        # Convertir DataFrame a JSON string
        amenities_json = amenities_df.to_json(orient='records')
        market_analysis_json = market_analysis_df.to_json(orient='records')

        # Empujar datos a XCom
        ti = kwargs['ti']
        ti.xcom_push(key='amenities_df', value=amenities_json)
        ti.xcom_push(key='market_analysis_df', value=market_analysis_json)

        logger.info('Data extraction complete')
    except Exception as e:
        logger.error('Failed during data extraction for data_etl task', exc_info=True)
        raise


def transform_data_etl(**kwargs):
    logger = logging.getLogger(__name__)
    logger.info('Starting data transformation for data_etl task')

    ti = kwargs['ti']
    amenities_json = ti.xcom_pull(task_ids='data_extract_task', key='amenities_df')
    market_analysis_json = ti.xcom_pull(task_ids='data_extract_task', key='market_analysis_df')

    amenities_df = pd.read_json(amenities_json)
    market_analysis_df = pd.read_json(market_analysis_json)

    logger.info(f'Amenities JSON received: {amenities_df.head()}')
    logger.info(f'Market analysis JSON received: {market_analysis_df.head()}')
    
    try:
        merged_df = pd.merge(amenities_df, market_analysis_df, on='unified_id', how='inner')

        merged_df['guests'] = merged_df['guests'].replace('15+', 15)
        merged_df['guests'] = pd.to_numeric(merged_df['guests'])

        merged_df['bathrooms'] = merged_df['bathrooms'].astype(float)
        merged_df['bedrooms'] = merged_df['bedrooms'].astype(float)
        merged_df['openness'] = merged_df['openness'].astype(float)

        merged_df['revenue'] = merged_df['revenue'].str.replace(',', '.')
        merged_df['revenue'] = pd.to_numeric(merged_df['revenue'])

        merged_df['occupancy'] = merged_df['occupancy'].str.replace(',', '.')
        merged_df['occupancy'] = pd.to_numeric(merged_df['occupancy'])

        merged_df['nightly rate'] = merged_df['nightly rate'].str.replace(',', '.')
        merged_df['nightly rate'] = pd.to_numeric(merged_df['nightly rate'])

        merged_df['lead time'] = merged_df['lead time'].str.replace(',', '.').astype(float)
        merged_df['length stay'] = merged_df['length stay'].str.replace(',', '.')
        merged_df['length stay'] = pd.to_numeric(merged_df['length stay'])

        merged_df.rename(columns={
            'nightly rate': 'nightly_rate',
            'lead time': 'lead_time',
            'length stay': 'length_stay'
        }, inplace=True)

        merged_df['length_stay'].fillna(merged_df['length_stay'].mean(), inplace=True)
        merged_df['lead_time'].fillna(merged_df['lead_time'].mean(), inplace=True)
        merged_df['revenue'].fillna(merged_df['revenue'].mean(), inplace=True)
        merged_df['nightly_rate'].fillna(merged_df['nightly_rate'].mean(), inplace=True)
        
        numeric_cols = merged_df.select_dtypes(include=['int64', 'float64', 'int32']).columns

        # Outliers Handling
        for col in numeric_cols:
            Q1 = merged_df[col].quantile(0.25)
            Q3 = merged_df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            merged_df[col] = np.where(merged_df[col] < lower_bound, lower_bound, merged_df[col])
            merged_df[col] = np.where(merged_df[col] > upper_bound, upper_bound, merged_df[col])
        
        if 'month_y' in merged_df.columns:
            merged_df.drop(columns=['month_y'], inplace=True)
        if 'month_x' in merged_df.columns:
            merged_df.rename(columns={'month_x': 'month'}, inplace=True)

        logger.info(f'Data transformed successfully:\n{merged_df.head()}')

        # Convertir DataFrame a JSON y empujar a XCom
        data_json = merged_df.head(15000).to_json(orient='records')
        ti.xcom_push(key='data_etl', value=data_json)

        logger.info('Data transformation complete')
    except Exception as e:
        logger.error('Failed during data transformation for data_etl task', exc_info=True)
        raise