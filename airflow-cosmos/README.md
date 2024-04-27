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

## Manual Configuration After Container Creation

After creating the container, perform the following manual configurations:

### 1. Open a browser and navigate to `http://127.0.0.1:8000` to access the Airflow UI.

### 2. From the Airflow UI, select "Admin" from the menu and then choose "Connections".

### 3. Click the "Create" button to create a new connection.

### 4. Configure the connection with the following details:
   - `Conn Id`: `airflow_db`
   - `Conn Type`: `Postgres`
   - `Host`: Database hostname (e.g., host.docker.internal)
   - `Port`: Database port number
   - `Password`: Database password
   - `Database`: Database name
   - `Login`: Database username

Run the following command to execute the Airflow Webserver and Scheduler:

```bash
source airflow/dbt_venv/bin/activate && airflow webserver --port 8080 & airflow scheduler
```
