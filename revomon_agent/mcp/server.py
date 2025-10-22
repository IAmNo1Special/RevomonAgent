import asyncio
import json
import logging
import os
import sys

# Add the project root to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure logging
log_dir = "revomon_agent/logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "revomonauto_mcp_server.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=log_file,
    filemode="a",
)
logger = logging.getLogger(__name__)

import mcp.server.stdio
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type
from mcp import types as mcp_types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

from revomon_agent.configs.mcp import mcp_config

app = Server("revomonauto_mcp")


# Implement the MCP server's handler to list available tools
@app.list_tools()
async def list_mcp_tools() -> list[mcp_types.Tool]:
    """MCP handler to list tools this server exposes."""
    logger.info("Received list_tools request.")
    # Convert the ADK tool's definition to the MCP Tool schema format
    mcp_tools_schemas = []
    for function_tool in mcp_config.MCP_FUNCTION_TOOLS:
        mcp_tool = adk_to_mcp_tool_type(function_tool)
        mcp_tools_schemas.append(mcp_tool)
    logger.info("RevomonAuto tools advertised.")
    return mcp_tools_schemas


# Implement the MCP server's handler to execute a tool call
@app.call_tool()
async def call_mcp_tool(name: str, arguments: dict) -> list[mcp_types.Content]:
    """MCP handler to execute a tool call requested by an MCP client."""
    logger.info(f"Received call_tool request for '{name}' with args: {arguments}")

    # Check if the requested tool name matches our wrapped ADK too
    tool = mcp_config.MCP_TOOL_MAP.get(name)
    if tool is None:
        logger.warning(f"Tool '{name}' not found/exposed by this server.")
        error_text = json.dumps(
            {"error": f"Tool '{name}' not implemented by this server."}
        )
        return [mcp_types.TextContent(type="text", text=error_text)]

    try:
        # Note: tool_context is None here because this MCP server is
        # running the ADK tool outside of a full ADK Runner invocation.
        # If the ADK tool requires ToolContext features (like state or auth),
        # this direct invocation might need more sophisticated handling.
        adk_tool_response = await tool.run_async(args=arguments, tool_context=None)
        logger.info(f"ADK tool '{name}' executed. Response: {adk_tool_response}")

        response_text = json.dumps(adk_tool_response, indent=2)
        return [mcp_types.TextContent(type="text", text=response_text)]

    except Exception as e:
        logger.error(f"Error executing ADK tool '{name}': {e}")
        # Return an error message in MCP format
        error_text = json.dumps({"error": f"Failed to execute tool '{name}': {str(e)}"})
        return [mcp_types.TextContent(type="text", text=error_text)]


async def run_mcp_stdio_server():
    """Runs the MCP server, listening for connections over standard input/output."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        logger.info("Starting handshake with client.")
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=app.name,
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    # Define server capabilities - consult MCP docs for options
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        logger.info("Run loop finished or client disconnected.")


if __name__ == "__main__":
    logger.info("Launching MCP Server to expose ADK tools via stdio.")
    try:
        asyncio.run(run_mcp_stdio_server())
    except KeyboardInterrupt:
        logger.info("MCP Server stopped by user.")
    except Exception as e:
        logger.error(f"MCP Server encountered an error: {e}")
    finally:
        logger.info("MCP Server process exiting.")
