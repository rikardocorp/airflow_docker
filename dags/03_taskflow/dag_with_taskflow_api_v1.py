import os
import pytz
from datetime import datetime, timedelta

from airflow.decorators import dag, task

# Obtener la zona horaria deseada
TZ = os.getenv('TZ')
timezone = pytz.timezone(TZ)

default_args = {
    'owner': 'datapath',
    # 'retries': 5,
    # 'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id='dag_with_taskflow_api_v1',
    default_args=default_args, 
    start_date=datetime(2023, 6, 28, tzinfo=timezone), 
    schedule_interval='@once',
    catchup=False,
    schedule=None,
)
def hello_world_etl():
    # @task()
    # def get_name() -> dict[str,str]:
    #     return {'first_name': 'Jerry', 'last_name': 'Fridman'}

    @task(multiple_outputs=True)
    def get_name():
        return {'first_name': 'Jerry', 'last_name': 'Fridman'}

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")
    
    name_dict = get_name()
    age = get_age()
    greet(
        first_name=name_dict['first_name'], 
        last_name=name_dict['last_name'],
        age=age
    )

greet_dag = hello_world_etl()