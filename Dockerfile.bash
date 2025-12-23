FROM ubuntu:22.04

WORKDIR /app

# Instalează tool-urile necesare
RUN apt-get update && apt-get install -y bash iproute2 bc wget iputils-ping

# Copiază scriptul monitor
COPY bash_script/monitor.sh .

# Permisiuni
RUN chmod +x monitor.sh

# Rulează scriptul în loop continuu
CMD ["bash", "-c", "while true; do ./monitor.sh; sleep 5; done"]
