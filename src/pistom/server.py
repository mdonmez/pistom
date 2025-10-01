import httpx
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Define the global server object. The runtime will find this.
mcp = FastMCP("Pistom MCP Server")


@mcp.tool()
async def run_python_code(code: str) -> Optional[str]:
    """
    Executes given Python code with Python 3.10.0 interpreter.
    ... (docstring content) ...
    """
    payload = {"language": "python", "version": "3.10.0", "files": [{"content": code}]}

    try:
        # Crucially, this must be async/await
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                "https://emkc.org/api/v2/piston/execute", json=payload
            )
            response.raise_for_status()
            return response.json().get("run", {}).get("output", "")
    except (httpx.RequestError, httpx.HTTPStatusError, KeyError) as e:
        return f"Error: {e}"