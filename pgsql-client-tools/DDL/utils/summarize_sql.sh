#!/bin/sh

TARGET_DIR="pgsql-client-tools/DDL/sql"

OUTPUT_FILE="${TARGET_DIR}/summarized.sql"

if [ -f "$OUTPUT_FILE" ]; then
    rm "$OUTPUT_FILE"
fi

for file in ${TARGET_DIR}/*.sql; do
    echo $file
    cat "$file" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done
