from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters

from ...callbacks import inject_world_state, update_internal_worldstate
from ...configs.mcp import mcp_config
from ...toolbox.tools import (
    close_revomon_app,
    log_in_revomon,
    open_revomon_app,
    quit_game,
    start_revomon_game,
)
from .descriptions import app_launcher_description
from .instructions import app_launcher_instructions

load_dotenv()


def create_app_launcher_agent(use_mcp_tools: bool = False) -> Agent:
    tools = []

    if use_mcp_tools:
        mcp_toolset = McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="python",
                    args=[
                        mcp_config.MCP_SERVER_SCRIPT,
                    ],
                ),
                timeout=300,
            ),
            tool_filter=[
                "open_revomon_app",
                "close_revomon_app",
                "start_revomon_game",
                "log_in_revomon",
                "quit_game",
            ],
        )
        tools.append(mcp_toolset)
    else:
        tools.append(open_revomon_app)
        tools.append(close_revomon_app)
        tools.append(start_revomon_game)
        tools.append(log_in_revomon)
        tools.append(quit_game)

    app_launcher_agent = Agent(
        name="app_launcher_agent",
        model="gemini-2.5-flash",
        description=app_launcher_description,
        instruction=app_launcher_instructions,
        tools=tools,
        before_model_callback=[inject_world_state],
        after_tool_callback=[update_internal_worldstate],
    )

    return app_launcher_agent
