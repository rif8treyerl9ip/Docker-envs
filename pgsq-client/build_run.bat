docker build --tag pgsql-client -f pgsql-client-dockerfile .

docker run --rm -it --name pgsql-client pgsql-client
