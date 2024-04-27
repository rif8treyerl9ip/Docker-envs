from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 5),
}

dag_name = 'HELLOWORLD'

with DAG(dag_name, default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    # SQL定義を実行するタスク
    execute_sql = BashOperator(
        task_id='EXE_psqldef',
        bash_command="echo xxxxxxxxxxxxxxxxxxxxx",
    )
