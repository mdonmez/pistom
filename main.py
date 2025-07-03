import httpx
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Pistom MCP Server")


@mcp.tool()
def run_python_code(code: str) -> Optional[str]:
    """
    Executes given Python code with Python 3.10.0 interpreter.
    This tool is useful for solving math, coding, logical, and other problems.
    Example:
        Problem: Count the number of 'r' in the word 'strawberry'.
        Tool Input: print(f'{"strawberry".count("r")}')
        Tool Output: 3

    Args:
        code (str): The source code to execute.

    Returns:
        Optional[str]: Output from the code execution, or None if request fails.
    """
    payload = {"language": "python", "version": "3.10.0", "files": [{"content": code}]}

    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                "https://emkc.org/api/v2/piston/execute", json=payload
            )
            response.raise_for_status()
            return response.json().get("run", {}).get("output", "")
    except (httpx.RequestError, httpx.HTTPStatusError, KeyError) as e:
        return f"Error: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
