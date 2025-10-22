from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters

from ...callbacks import inject_world_state, update_internal_worldstate
from ...configs.mcp import mcp_config
from ...toolbox.tools import close_wardrobe, open_wardrobe
from .descriptions import wardrobe_agent_description
from .instructions import wardrobe_agent_instructions

load_dotenv()


def create_wardrobe_agent(use_mcp_tools: bool = False) -> Agent:
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
                "open_wardrobe",
                "close_wardrobe",
            ],
        )
        tools.append(mcp_toolset)
    else:
        tools.append(open_wardrobe)
        tools.append(close_wardrobe)

    wardrobe_agent = Agent(
        name="wardrobe_agent",
        model="gemini-2.5-flash",
        description=wardrobe_agent_description,
        instruction=wardrobe_agent_instructions,
        tools=tools,
        before_model_callback=[inject_world_state],
        after_tool_callback=[update_internal_worldstate],
    )

    return wardrobe_agent
