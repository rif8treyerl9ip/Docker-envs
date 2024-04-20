FROM alpine:latest

RUN apk add --no-cache tinyproxy

COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

RUN mkdir -p /var/run/tinyproxy /var/log/tinyproxy \
    && chown -R nobody:nogroup /var/run/tinyproxy /var/log/tinyproxy

EXPOSE 8888

CMD ["tinyproxy", "-d"]
