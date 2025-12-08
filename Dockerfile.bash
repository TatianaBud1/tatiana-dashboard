FROM ubuntu:22.04
WORKDIR /app
COPY bash_script/monitor.sh .
RUN apt-get update && apt-get install -y iputils-ping && chmod +x monitor.sh
CMD ["./monitor.sh"]
