from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters

from ...callbacks import inject_world_state, update_internal_worldstate
from ...configs.mcp import mcp_config
from ...toolbox.tools import close_settings, open_settings
from .descriptions import settings_agent_description
from .instructions import settings_agent_instructions

load_dotenv()


def create_settings_agent(use_mcp_tools: bool = False) -> Agent:
    tools = []
    if use_mcp_tools:
        mcp_toolset = McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="python",
                    args=[mcp_config.MCP_SERVER_SCRIPT],
                ),
                timeout=300,
            ),
            tool_filter=[
                "open_settings",
                "close_settings",
            ],
        )
        tools.append(mcp_toolset)
    else:
        tools.append(open_settings)
        tools.append(close_settings)

    settings_agent = Agent(
        name="settings_agent",
        model="gemini-2.5-flash",
        description=settings_agent_description,
        instruction=settings_agent_instructions,
        tools=tools,
        before_model_callback=[inject_world_state],
        before_tool_callback=[update_internal_worldstate],
        after_tool_callback=[update_internal_worldstate],
    )

    return settings_agent
