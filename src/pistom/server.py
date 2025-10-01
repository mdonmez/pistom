import httpx
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Pistom MCP Server")


@mcp.tool()
async def run_python_code(code: str) -> Optional[str]:
    """
    Executes given Python code with Python 3.10.0 interpreter.
    This tool is useful for solving math, coding, logical, and other problems that can be solved with Python.

    Args:
        code (str): The source code to execute.

    Returns:
        Optional[str]: Output from the code execution, or None if request fails.
    """
    payload = {"language": "python", "version": "3.10.0", "files": [{"content": code}]}

    try:
        # 1. CHANGE: Use httpx.AsyncClient
        async with httpx.AsyncClient(timeout=10.0) as client:
            # 2. CHANGE: Await the post request
            response = await client.post(
                "https://emkc.org/api/v2/piston/execute", json=payload
            )
            response.raise_for_status()
            return response.json().get("run", {}).get("output", "")
    except (httpx.RequestError, httpx.HTTPStatusError, KeyError) as e:
        return f"Error: {e}"


def main():
    mcp.run()


if __name__ == "__main__":
    main()
