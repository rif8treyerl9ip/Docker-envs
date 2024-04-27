
cd airflow-cosmos

echo DB_USER=%JQU1%>docker/.env
echo DB_PASS=%JQP%>>docker/.env
echo DB_NAME=%JQD%>>docker/.env

docker build -f ./docker/Dockerfile -t airflow-dbt .

docker run -it --rm ^
    --name airflow-dbt ^
    --user airflow ^
    --env-file docker/.env -p 8080:8080 ^
    -v %cd%/airflow/dags:/usr/local/airflow/dags ^
    -v %cd%/airflow/logs:/usr/local/airflow/logs ^
    -v %cd%/docker:/usr/local/docker ^
    airflow-dbt
