# Build the model
dbt run

dbt test

dbt docs generate

dbt docs serve --port 8090

dbt source snapshot-freshness

dbt snapshot
