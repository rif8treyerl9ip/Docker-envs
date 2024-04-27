FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -ms /bin/bash airflow \
    && usermod -aG sudo airflow

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    python3.10 \
    python3.10-dev \
    python3.10-distutils \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    sudo \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN /bin/bash -c "python3 -m venv /opt/dbt_venv && \
    source /opt/dbt_venv/bin/activate && \
    pip install apache-airflow \
    astronomer-cosmos \
    dbt-core \
    dbt-postgres \
    apache-airflow-providers-postgres \
    && deactivate"

ENV AIRFLOW_HOME=/usr/local/airflow \
    AIRFLOW__CORE__LOAD_EXAMPLES=false

USER root
RUN mkdir -p /usr/local/airflow/
RUN cp -r /opt/dbt_venv/ /usr/local/airflow/
RUN chown -R airflow:airflow /usr/local/airflow/
RUN chmod -R 775 /usr/local/
USER airflow

WORKDIR /usr/local/

EXPOSE 8080
