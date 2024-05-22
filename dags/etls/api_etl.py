import requests
import logging
import os
import pandas as pd
import re
import json

def extract_api_data(**kwargs):
    logger = logging.getLogger(__name__)
    logger.info('Starting data extraction for data_etl task')

    urls_tokens = [
        ("https://api.apify.com/v2/datasets/xblAhnLzFKh5s3upE/items", "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf"),
        ("https://api.apify.com/v2/datasets/hgh9xbDJVMbo14z3H/items", "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf"),
        ("https://api.apify.com/v2/datasets/GnngHjfOFgZ4OEWP8/items", "apify_api_TYX4DnZJ2wG4O3dxUuZ99lbz520t6w3f7dDf")
    ]

    for i, (url, token) in enumerate(urls_tokens):
        try:
            logger.info(f"Starting extraction from {url}")
            response = requests.get(url, params={"token": token})

            if response.status_code == 200:
                data = response.json()
                json_data = pd.DataFrame(data).to_json(orient='records')
                file_name = f"data_{i+1}.json"
                with open(file_name, "w") as f:
                    f.write(json_data)
                logger.info(f"Data extracted successfully from {url} and saved as {file_name}")
            else:
                logger.error(f"Error {response.status_code} when fetching data from {url}")
        except Exception as e:
            logger.error(f"Failed to extract data from {url}", exc_info=True)
            raise


def transform_api_data(**kwargs):
    logger = logging.getLogger(__name__)
    logger.info('Starting transformation of API data')

    try:
        datasets = []

        for i in range(3):
            file_name = f"data_{i+1}.json"
            with open(file_name, "r") as f:
                data = json.load(f)
                datasets.append(pd.DataFrame(data))

        merged_df = pd.concat(datasets, ignore_index=True)

        columns_to_drop = ['photos', 'primaryHost', 'additionalHosts', 'isHostedBySuperhost', 
                           'calendar', 'url', 'id', 'location', 'reviews', 'isAvailable']
        merged_df = merged_df.drop(columns=columns_to_drop)

        merged_df['nightly_rate'] = merged_df['pricing'].str.extract(r"'amount'\s*:\s*(\d+)")
        merged_df = merged_df.drop(columns=['pricing'])

        merged_df.rename(columns={
            'numberOfGuests': 'guests',
            'address': 'city',
            'occupancyPercentage': 'openness'
        }, inplace=True)

        merged_df['city'] = merged_df['city'].apply(lambda x: x.split(',')[0])

        merged_df['guests'] = pd.to_numeric(merged_df['guests'], errors='coerce').astype(float)
        merged_df['nightly_rate'] = pd.to_numeric(merged_df['nightly_rate'], errors='coerce').astype(float)
        merged_df['nightly_rate'] = merged_df['nightly_rate'].round(2)
        merged_df['openness'] = pd.to_numeric(merged_df['openness'], errors='coerce').astype(float)
        merged_df['openness'] = merged_df['openness'].round(2)

        logger.info(f"Shape of the resulting DataFrame: {merged_df.shape}")

        api_json = merged_df.to_json(orient='records')
        ti = kwargs['ti']
        ti.xcom_push(key='api_data', value=api_json)

        logger.info('API data transformation complete')
    except Exception as e:
        logger.error('Failed during the transformation of API data', exc_info=True)
        raise