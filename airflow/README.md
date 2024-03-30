# Utilizing Apache Airflow with Docker Compose

To run Apache Airflow within Docker containers, using Docker Compose is a convenient approach. The [official Apache Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) provides a detailed guide on how to initiate Airflow using Docker Compose.

## Docker Compose Commands

Utilize Docker Compose to launch Airflow containers.

```bash
set AIRFLOW_PROJ_DIR=C:\path\to\your\airflow-project
docker-compose build --no-cache
docker-compose up
```

### Removing All Containers and Volumes, Building Images

```bash
docker-compose down --volumes --rmi all
```
