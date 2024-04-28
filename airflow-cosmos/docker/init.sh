#!/bin/bash

rm docker/.env

export DBT_PROFILE_DIR='/usr/local/airflow/dags/dbt'

airflow db init

airflow users create \
    --username admin \
    --password admin \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email admin@example.com

source /usr/local/airflow/dbt_venv/bin/activate

airflow connections delete 'airflow_db'
airflow connections add 'airflow_db' \
    --conn-type 'postgres' \
    --conn-host 'host.docker.internal' \
    --conn-schema $DB_NAME \
    --conn-login $DB_USER \
    --conn-password $JQP \
    --conn-port '5432'

airflow connections add 'test_slack' \
    --conn-type 'slackwebhook' \
    --conn-host 'https://hooks.slack.com/services' \
    --conn-schema '' \
    --conn-login '' \
    --conn-password $SLACK_WEBHOOK

sed -i 's|^default_timezone = .*|default_timezone = Asia/Tokyo|' airflow/airflow.cfg
sed -i 's/load_examples = True/load_examples = False/' airflow/airflow.cfg

# airflow connections get airflow_db
# airflow connections get test_slack
