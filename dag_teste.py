from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_info():
    print("Esta é uma tarefa de exemplo que imprime algumas informações.")
    print("Data e hora atual:", datetime.now())

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG('exemplo_dag', 
         default_args=default_args, 
         description='Uma DAG de exemplo que imprime informações',
         schedule_interval='@daily',
         catchup=False) as dag:

    task_print_info = PythonOperator(
        task_id='print_info',
        python_callable=print_info
    )

task_print_info
