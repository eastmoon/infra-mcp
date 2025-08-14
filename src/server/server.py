"""
FastMCP server configuration.
"""

# Import system libraries
import os
# Import MCP libraries
from mcp.server.fastmcp import FastMCP
# Accessing an environment variable
env_mcp_server_name = os.environ['MCP_SERVER_NAME']
# Create an MCP server
mcp = FastMCP(f"{env_mcp_server_name}")
mcp.settings.host = "0.0.0.0"
mcp.settings.port = 80
