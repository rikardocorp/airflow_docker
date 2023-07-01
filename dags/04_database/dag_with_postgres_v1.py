from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'datapath',
}

with DAG(
    dag_id='dag_with_postgres_operator_v1',
    default_args=default_args,
    start_date=datetime(2023, 6, 28),
    schedule_interval='@once',
    catchup=False,
    schedule=None
) as dag:
    
    task1 = PostgresOperator(
        task_id='create_pet_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            CREATE TABLE IF NOT EXISTS pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            OWNER VARCHAR NOT NULL);
        """
    )

    task2 = PostgresOperator(
        task_id='insert_into_table_1',
        postgres_conn_id='postgres_localhost',
        sql="""
            INSERT INTO pet (name, pet_type, birth_date, OWNER)  VALUES ( 'Max', 'Dog', '2018-07-05', 'Jane');
            INSERT INTO pet (name, pet_type, birth_date, OWNER)  VALUES ( 'Susie', 'Cat', '2019-05-01', 'Phil');
        """
    )

    task3 = PostgresOperator(
        task_id='insert_into_table_2',
        postgres_conn_id='postgres_localhost',
        sql="""
            INSERT INTO pet (name, pet_type, birth_date, OWNER) VALUES ( 'Lester', 'Hamster', '2020-06-23', 'Lily');
            INSERT INTO pet (name, pet_type, birth_date, OWNER) VALUES ( 'Quincy', 'Parrot', '2013-08-11', 'Anne');
        """
    )

    task4 = PostgresOperator(
        task_id='get_all_pets',
        postgres_conn_id='postgres_localhost',
        sql="""
            SELECT * FROM pet;
        """
    )

    task5 = PostgresOperator(
        task_id='get_birth_date',
        postgres_conn_id='postgres_localhost',
        sql="SELECT * FROM pet WHERE birth_date BETWEEN SYMMETRIC %(begin_date)s AND %(end_date)s",
        parameters={"begin_date": "2020-01-01", "end_date": "2020-12-31"},
    )

    task1 >> [task2, task3] >> task4 >> task5