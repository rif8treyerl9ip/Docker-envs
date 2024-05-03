#!/bin/sh

echo "Please enter your password: "
read -s PSQLDEF_PASSWORD

export PSQLDEF_PASSWORD

TARGET_DIR="pgsql-client-tools/DDL/sql"

psqldef --host=host.docker.internal --port=5432 --user="$JQ_U1" --password="$JQP" "$JQD" --dry-run < pgsql-client-tools/DDL/sql/summarized.sql

