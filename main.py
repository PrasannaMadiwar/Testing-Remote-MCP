from fastmcp import FastMCP

mcp = FastMCP("sample-tools")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Add two integers and return the result.
    """
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
