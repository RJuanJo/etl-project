import pandas as pd
import logging

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

        for column in ['hot_tub', 'pool', 'bedrooms', 'bathrooms', 'revenue', 'occupancy', 'lead_time', 'length_stay']:
            median_value = merged_df[column].median()
            merged_df[column] = merged_df[column].fillna(median_value)

        logger.info(f'Merged DataFrame shape: {merged_df.shape}')
        logger.info(f'Merged DataFrame preview:\n{merged_df.head()}')
        logger.info(f'Merged DataFrame preview:\n{merged_df.info()}')


        logger.info('Data merge complete')
    except Exception as e:
        logger.error('Failed during merging of data', exc_info=True)
        raise