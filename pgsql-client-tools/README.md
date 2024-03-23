# PSQL Toolkit Docker Image

## Key Features

- postgresql-client: Command-line access to PostgreSQL servers.
- [@dbml/cli](https://www.npmjs.com/package/@dbml/cli): A CLI tool specifically designed for converting between DBML files and SQL scripts, facilitating database schema management.
- [psqldef](https://github.com/sqldef/sqldef): A tool for managing database schemas.

## How to Use

### 1. Docker Build & Run

```bash
pgsql-client-tools/Docker/build_run.bat
```

### 2. Creating DDL
Developers create DDL files in the `pgsql-client-tools\DDL\sql` directory.

### 3. Converting to DBML format
To convert the created DDL files to DBML format, run the following script:

```sh
pgsql-client-tools/DDL/utils/convert_sql_to_dbml.sh
```
At this stage, before proceeding to step 3, you need to consolidate the contents of the generated dbml files into a single dbml file.

### 4. Creating ER using dbdocs
```
dbdocs build pgsql-client-tools/DDL/dbml/summarized.dbml
```
