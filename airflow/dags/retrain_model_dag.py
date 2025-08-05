from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from src.clean.clean_air_quality import clean_air_data
from src.features.engineer import engineer_features
from src.models.train_model import train_model

def retrain():
    df = pd.read_csv("data/raw/air_quality.csv")
    df = clean_air_data(df)
    df = engineer_features(df)
    train_model(df)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

dag = DAG(
    'retrain_model_daily',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

retrain_task = PythonOperator(
    task_id='retrain_model',
    python_callable=retrain,
    dag=dag
)