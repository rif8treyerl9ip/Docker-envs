from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# この関数が"Hello World"を5回出力します
def print_hello():
    for _ in range(5):
        print("TEST")

# DAGのデフォルト引数を設定します
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAGを定義します
dag = DAG(
    'hello_world_dag', # DAGの名前です
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='49 14 * * 5', # 毎週金曜日のUTC 14:48（JST 23:48）に実行されるようにスケジュールします
)

# PythonOperatorを使用して、上記のprint_hello関数をタスクとしてDAGに追加します
t1 = PythonOperator(
    task_id='print_hello', # タスクのIDです
    python_callable=print_hello, # 実行するPython関数を指定します
    dag=dag, # このタスクを追加するDAGを指定します
)

# DAGの中でタスクを実行する順序を定義します
# ここではt1タスクが単独で実行されるため、特に順序を設定する必要はありません
