from airflow.decorators import task, dag
from datetime import datetime

@task
def add_task(x, y):
    print(f"Task args: x={x}, y={y}")
    return x + y

@dag(
    dag_id='dag_with_taskflow_api_v2_1',
    start_date=datetime(2022, 1, 1), schedule=None)
def mydag():
    start = add_task.override(task_id="start")(1, 2)
    for i in range(3):
        start >> add_task.override(task_id=f"add_start_{i}")(start, i + 1)


@dag(
    dag_id='dag_with_taskflow_api_v2_2',
    start_date=datetime(2022, 1, 1), schedule=None)
def mydag2():
    start = add_task(1, 2)
    for i in range(3):
        start = add_task(start, i + 1)


first_dag = mydag()
second_dag = mydag2()

