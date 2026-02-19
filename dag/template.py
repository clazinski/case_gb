from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime, timedelta
from pathlib import Path

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

SQL_PATH = Path('/opt/airflow/dags/sql_scripts/datasets/analytics/vendas_por_linha_data.sql') #exemplo

def read_sql(sql_path):
    """Lê arquivo SQL"""
    if not sql_path.exists():
        raise FileNotFoundError(f"SQL não encontrado: {sql_path}")
    
    with open(sql_path, 'r', encoding='utf-8') as file:
        return file.read()

with DAG(
    'execute_sql_bigquery',
    default_args=default_args,
    description='DAG para executar scripts SQLs no BigQuery - dataset analytics',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['bigquery', 'sql'],
) as dag:
    
    execute_query = BigQueryInsertJobOperator(
        task_id='execute_sql_bigquery',
        configuration={
            "query": {
                "query": read_sql(SQL_PATH),
                "useLegacySql": False,
                "destinationTable": {
                    "projectId": "elevated-bonito-485002-k9",
                    "datasetId": "analytics",
                    "tableId": "vendas_por_linha_data"
                },
                "writeDisposition": "WRITE_TRUNCATE",
            }
        },
        location='US',
        gcp_conn_id='google_cloud_default',
    )
    
    execute_query
