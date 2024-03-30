docker build -t dbt-alpine -f Docker/Dockerfile .

docker run --rm -it ^
  -p 8080:8080 ^
  -e DB_HOST='localhost' ^
  -e DB_PORT=5432 ^
  -e DB_USER=%JQU1% ^
  -e DB_PASS=%JQP% ^
  -e DB_NAME=%JQD% ^
  -v %CD%/profiles.yml:/root/.dbt/profiles.yml ^
  -v "%CD%:/workspace" ^
  dbt-alpine /bin/sh
