FROM node:22

RUN npm install -g @modelcontextprotocol/inspector

# COMMAND
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh
