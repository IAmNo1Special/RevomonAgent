from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters

from ...callbacks import inject_world_state, update_internal_worldstate
from ...configs.mcp import mcp_config
from ...toolbox.tools import close_discussion, open_discussion
from .descriptions import discussion_agent_description
from .instructions import discussion_agent_instructions

load_dotenv()


def create_discussion_agent(use_mcp_tools: bool = False) -> Agent:
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
                "open_discussion",
                "close_discussion",
            ],
        )
        tools.append(mcp_toolset)
    else:
        tools.append(open_discussion)
        tools.append(close_discussion)

    discussion_agent = Agent(
        name="discussion_agent",
        model="gemini-2.5-flash",
        description=discussion_agent_description,
        instruction=discussion_agent_instructions,
        tools=tools,
        before_model_callback=[inject_world_state],
        before_tool_callback=[update_internal_worldstate],
        after_tool_callback=[update_internal_worldstate],
    )

    return discussion_agent
