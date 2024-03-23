#!/bin/sh

TARGET_DIR="pgsql-client-tools/DDL/sql"

find "$TARGET_DIR" -type f -name "*.sql" -exec sh -c '
  for sql_file do
    dbml_file="${sql_file%.sql}.dbml"
    dbml_file=$(echo "$dbml_file" | sed "s|/sql/|/dbml/|")
    echo "Converting $sql_file to $dbml_file"
    sql2dbml "$sql_file" -o "$dbml_file"
  done
' sh {} +

