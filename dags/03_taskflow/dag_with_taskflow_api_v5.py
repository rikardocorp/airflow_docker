import sys
from airflow.decorators import dag, task
from datetime import datetime

@task(multiple_outputs=True)
def transform(order_data_dict: dict):

    import sys
    print("Python Version")
    print(sys.version)
    print("-----------")

    total_order_value = 0
    for value in order_data_dict.values():
        total_order_value += value
    
    print("total_order_value:", total_order_value)
    return {"total_order_value": total_order_value}


@task.docker(image="python:3.9-slim-bullseye", multiple_outputs=True)
def transform_docker(order_data_dict: dict):

    import sys
    print("Python Version")
    print(sys.version)
    print("-----------")
    
    total_order_value = 0
    for value in order_data_dict.values():
        total_order_value += value

    print("total_order_value:", total_order_value)
    return {"total_order_value": total_order_value}


@dag(
    dag_id='dag_with_taskflow_api_v5',
    start_date=datetime(2022, 1, 1),
    schedule=None
)
def mydag():
    
    transform({'cafe': 3, 'sandwich': 5, 'salad': 10})
    transform_docker({'cafe': 3, 'sandwich': 5, 'salad': 10})


first_dag = mydag()
