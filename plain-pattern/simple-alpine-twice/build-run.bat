docker build -f Dockerfile1 -t alpine-minimum .
docker build -f Dockerfile2 -t alpine-minimum-tmux .


@REM docker run -it alpine-ping /bin/sh
@REM docker run -it alpine-ping-editors /bin/sh
docker images
