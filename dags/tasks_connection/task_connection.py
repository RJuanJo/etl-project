from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.abspath("/opt/airflow/dags/"))

from etls.api_etl import extract_api_data, transform_api_data
from etls.data_etl import extract_data_etl, transform_data_etl
from etls.merge_data import merge_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 4),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'project_dag',
    default_args=default_args,
    description='A DAG for extracting, transforming, and loading data',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    api_extract_task = PythonOperator(
        task_id='extract_api_task',
        python_callable=extract_api_data
    )

    api_transform_task = PythonOperator(
        task_id='transform_api_task',
        python_callable=transform_api_data,
        provide_context=True
    )

    data_extract_task = PythonOperator(
        task_id='data_extract_task',
        python_callable=extract_data_etl,
        provide_context=True
    )

    data_transform_task = PythonOperator(
        task_id='transform_data_task',
        python_callable=transform_data_etl,
        provide_context=True
    )

    merge_task = PythonOperator(
        task_id='merge_data_task',
        python_callable=merge_data,
        provide_context=True
    )

    api_extract_task >> api_transform_task >> merge_task
    data_extract_task >> data_transform_task >> merge_task
