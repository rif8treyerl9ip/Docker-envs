![Cosmos Logo](https://raw.githubusercontent.com/astronomer/astronomer-cosmos/main/docs/_static/cosmos-logo.svg)

-------------------

## Setting up an Environment with Airflow and DBT

Follow these steps to set up an environment that includes Airflow and DBT:

### 1. Navigate to the Repository Root Directory

```bash
cd airflow-cosmos
```

### 2. Create a `.env` File Containing Environment Variables

```bash
echo DB_USER=%JQU1%>docker/.env
echo DB_PASS=%JQP%>>docker/.env
echo DB_NAME=%JQD%>>docker/.env
```

### 3. Build the Docker Image

```bash
docker build -f ./docker/Dockerfile -t airflow-dbt .
```

### 4. Run the Docker Container

```bash
docker run -it --rm ^
    --name airflow-dbt ^
    --user airflow ^
    --env-file docker/.env -p 8080:8080 ^
    -v %cd%/airflow/dags:/usr/local/airflow/dags ^
    -v %cd%/airflow/logs:/usr/local/airflow/logs ^
    -v %cd%/docker:/usr/local/docker ^
    airflow-dbt
```

## Initial Setup When Creating the Container

Run the following command initially when creating the container to initialize Airflow:

```bash
source airflow/dbt_venv/bin/activate && source ./docker/init.sh
```

Run the following command to execute the Airflow Webserver and Scheduler:

```bash
source airflow/dbt_venv/bin/activate && airflow webserver --port 8080 & airflow scheduler
```

## CLEANUP

When you're done working with the Airflow and DBT environment, follow these commands to clean up:

```bash

# terminate the Airflow-related processes
chmod +x docker/kill_airflow_processes.sh
ps aux && ./docker/kill_airflow_processes.sh

# Remove the Airflow logs
rm -rf /usr/local/airflow/logs/*

docker stop airflow-dbt
```
