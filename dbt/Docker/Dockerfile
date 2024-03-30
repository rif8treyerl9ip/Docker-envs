FROM alpine:latest

RUN apk add --no-cache python3 py3-pip python3-dev build-base libffi-dev git

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install dbt-postgres

WORKDIR /workspace

# Note: The password used here is weak and should be changed for production environments.
RUN adduser -D dbt && echo "dbt:dbt" | chpasswd
