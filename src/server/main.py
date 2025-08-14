"""
FastMCP server entrypoint.
"""

# Import server modules
from server import mcp
from tools import *
from resources import *
from prompts import *
# Python entrypoint program
if __name__ == "__main__":
    """Entry point for the direct execution server."""
    mcp.run(transport="streamable-http")
