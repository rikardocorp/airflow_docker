# airflow_docker
Despliegue de la Plataforma Airflow con Docker Compose sobre WSL2 - Windowds

# Instructions

## Resources
- mkdir project
- cd project
- git clone https://github.com/rikardocorp/airflow_docker
- rm -r -f ./logs
- mkdir -p ./dags ./logs ./plugins ./config

## Environments
- echo -e "AIRFLOW_UID=$(id -u)" > .env
- echo -e "TZ=America/Lima" >> .env
- echo -e "AIRFLOW__CORE__DEFAULT_TIMEZONE=America/Lima" >> .env
- echo -e "AIRFLOW__WEBSERVER__DEFAULT_UI_TIMEZONE=America/Lima" >> .env

## Deployment
- docker-compose up airflow-init
- docker-compose up -d
- docker ps
