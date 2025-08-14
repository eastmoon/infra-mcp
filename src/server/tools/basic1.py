from server import mcp

@mcp.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b
