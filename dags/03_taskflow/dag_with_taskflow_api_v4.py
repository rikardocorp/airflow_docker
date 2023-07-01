import sys
from airflow.decorators import dag
from datetime import datetime

PATH_COMMON = '../'
sys.path.append(PATH_COMMON)

from common.add_task import task_no_virtualenv, task_virtualenv, task_virtualenv_py2

@dag(
    dag_id='dag_with_taskflow_api_v4',
    start_date=datetime(2022, 1, 1),
    schedule=None
)
def mydag():
    task_no_virtualenv()

    task_virtualenv()

    task_virtualenv_py2()


first_dag = mydag()
