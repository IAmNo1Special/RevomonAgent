from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters

from ...callbacks import inject_world_state, update_internal_worldstate
from ...revomonagent_mcp.config import mcp_config
from ...toolbox.tools import close_friends_list, open_friends_list
from .descriptions import friends_list_agent_description
from .instructions import friends_list_agent_instructions

load_dotenv()


def create_friends_list_agent(use_mcp_tools: bool = False) -> Agent:
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
                "open_friends_list",
                "close_friends_list",
            ],
        )
        tools.append(mcp_toolset)
    else:
        tools.append(open_friends_list)
        tools.append(close_friends_list)

    friends_list_agent = Agent(
        name="friends_list_agent",
        model="gemini-2.5-flash",
        description=friends_list_agent_description,
        instruction=friends_list_agent_instructions,
        tools=tools,
        before_model_callback=[inject_world_state],
        after_tool_callback=[update_internal_worldstate],
    )

    return friends_list_agent
