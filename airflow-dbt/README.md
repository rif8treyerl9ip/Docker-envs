# Airflow and dbt Project Setup Guide

This guide outlines the setup process for projects using Airflow and dbt.
It is assumed that you are executing these instructions from within the `airflow-dbt` directory.

## Prerequisites

Before starting the project, ensure Docker and Docker Compose are installed. If you're on Windows, you can use Docker Desktop.

## Setup Instructions

1. **Navigate to the project directory.**

   ```cmd
   cd airflow-dbt
   ```

2. **Set the following environment variables:**

   ```cmd
   set AIRFLOW_PROJ_DIR=../../airflow
   set DB_USER=your_database_username
   set DB_PASS=your_database_password
   set DB_NAME=your_database_name
   ```

3. **Use Docker Compose to build images and start containers:**

   ```cmd
   docker-compose -f ./shared/Docker/docker-compose.yaml build
   docker-compose -f ./shared/Docker/docker-compose.yaml up
   ```

4. **To enter the dbt container, run the following command:**

   ```cmd
   shared\Docker\exec-docker-dbt.bat
   ```

   **Start the dbt server:**

   ```bash
   ./dbt_commands.sh
   ```

   **You can access the Airflow and dbt servers at the following URLs:**

   - Airflow: http://127.0.0.1:8080/
   - dbt: http://127.0.0.1:8090/

5. **Cleanup after use:**

   - Stop and remove all running Docker containers:

     ```cmd
     FOR /f "tokens=*" %i IN ('docker ps -aq') DO docker stop %i
     FOR /f "tokens=*" %i IN ('docker ps -aq') DO docker rm %i
     ```

   - Stop containers and remove volumes and images:

     ```cmd
     docker-compose -f ./shared/Docker/docker-compose.yaml down --volumes --rmi all
     ```
