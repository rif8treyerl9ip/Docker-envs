#!/bin/bash

rm docker/.env

export DBT_PROFILE_DIR='/airflow/dags/dbt'

airflow db init

airflow users create \
    --username admin \
    --password admin \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email admin@example.com
