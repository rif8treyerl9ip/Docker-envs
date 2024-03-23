docker build --tag pgsql-client-tools -f pgsql-client-dockerfile .

docker run \
    -e JQ_USER="%JQ_USER%" ^
    -e JQ_DB="%JQ_DB%" ^
    -v "%CD%:/workspace" \
    --rm -it --name pgsql-client-toolbox pgsql-client-tools
