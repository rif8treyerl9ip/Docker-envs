# PSQL Toolkit Docker Image

## Key Features

- postgresql-client: Command-line access to PostgreSQL servers.
- [psqldef](https://github.com/sqldef/sqldef): A tool for managing database schemas.

## How to Use

```bash
pgsql-client-tools/Docker/build_run.bat
```
psqldef --version
psql -h host.docker.internal -p 5432 -U $JQ_USER -d $JQ_DB

psqldef --host=host.docker.internal --port=5432 --user=$JQ_USER --password=<passwd> $JQ_DB --export
psqldef --host=host.docker.internal --port=5432 --user=$JQ_USER --password=<passwd> $JQ_DB --dry-run < pgsql-client-tools/DDL/query1.sql
psqldef --host=host.docker.internal --port=5432 --user=$JQ_USER --password=<passwd> $JQ_DB --dry-run < pgsql-client-tools/DDL/query2.sql
```
