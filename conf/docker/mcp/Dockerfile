FROM python:bullseye

USER root
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN echo "source $HOME/.local/bin/env" >> ~/.bashrc
RUN pip install "mcp[cli]"

# COMMAND
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh

# Set Environmnet
ENV MCP_SERVER_NAME="MCP Server"

# Setting Container
ENTRYPOINT ["bash", "docker-entrypoint.sh"]
