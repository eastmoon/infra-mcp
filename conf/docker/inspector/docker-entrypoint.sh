#!/bin/sh
set -e

# Run command with node if the first argument contains a "-" or is not a system command. The last
# part inside the "{}" is a workaround for the following bug in ash/dash:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=874264

if [ "${1#-}" != "${1}" ] || [ -z "$(command -v "${1}")" ] || { [ -f "${1}" ] && ! [ -x "${1}" ]; }; then
    set -- node "$@"
fi

if [ "${1}" = "node" ]; then
    openssl rand -hex 32 > /var/local/mcp.inspector.token
    MCP_PROXY_AUTH_TOKEN=$(cat /var/local/mcp.inspector.token) HOST=0.0.0.0 npx @modelcontextprotocol/inspector --transport http --server-url http://mcp-server/mcp
fi

exec "$@"
