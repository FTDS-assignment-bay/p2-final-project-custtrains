from airflow.models import DAG

from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime, timedelta

from utils.fetch_data import fetch_data_from_postgres
from utils.data_cleaning import clean_data

default_args = {
    'owner': 'Teguh', 
    'start_date': datetime(2024, 4, 27, 11, 00) - timedelta(hours=7),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
} 

with DAG(
    "Fetch_Clean_Data_DAG", # atur sesuai nama project kalian 
    description='Customer_Segmentation',
    schedule_interval='0 0 1 * *', # monthly / every 1st of the month.  
    default_args=default_args, 
    catchup=False) as dag:

    # Task: 1 
    fetching_data = PythonOperator(
        task_id='fetching_data',
        python_callable=fetch_data_from_postgres) 
    
    # Task: 2
    preprocess_data = PythonOperator(
        task_id='transform_and_predict',
        python_callable=clean_data)

    # Airflow process
    fetching_data >> preprocess_data