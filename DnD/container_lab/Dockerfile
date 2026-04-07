# linux base
FROM alpine:latest

# bash install
RUN apk add --no-cache bash

COPY crier.sh /usr/local/bin/crier.sh
COPY encounters.txt /usr/local/bin/encounters.txt
WORKDIR /usr/local/bin
RUN chmod +x /usr/local/bin/crier.sh
CMD ["/usr/local/bin/crier.sh"]
