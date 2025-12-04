FROM ubuntu:22.04
WORKDIR /app
COPY bash_script/monitor.sh .
RUN chmod +x monitor.sh
CMD ["./monitor.sh"]
