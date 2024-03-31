@echo off
FOR /f "tokens=1,2" %%i IN ('docker ps --format "{{.ID}} {{.Image}}" ^| findstr "docker-dbt"') DO (
    docker exec -it %%i sh
)
