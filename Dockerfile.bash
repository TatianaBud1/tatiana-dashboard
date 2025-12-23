FROM ubuntu:22.04
WORKDIR /app
RUN apt-get update && apt-get install -y bash iproute2 bc wget
COPY bash_script/monitor.sh .
RUN apt-get update && apt-get install -y iputils-ping && chmod +x monitor.sh
RUN chmod +x monitor.sh

CMD ["sh", "-c", "while true; do ./monitor.sh; sleep 5; done"]