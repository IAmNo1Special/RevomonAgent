from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters

from ...callbacks import inject_world_state, update_internal_worldstate
from ...configs.mcp import mcp_config
from ...toolbox.tools import (
    close_attacks_menu,
    enter_revomon_pvp_queue,
    exit_revomon_pvp_queue,
    open_attacks_menu,
    run_from_current_battle,
    toggle_auto_run_feat,
)
from .descriptions import pvp_agent_description
from .instructions import pvp_agent_instructions

load_dotenv()


def create_pvp_agent(use_mcp_tools: bool = False) -> Agent:
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
                "enter_revomon_pvp_queue",
                "exit_revomon_pvp_queue",
                "open_attacks_menu",
                "close_attacks_menu",
                "run_from_current_battle",
                "toggle_auto_run_feat",
            ],
        )
        tools.append(mcp_toolset)
    else:
        tools.append(enter_revomon_pvp_queue)
        tools.append(exit_revomon_pvp_queue)
        tools.append(open_attacks_menu)
        tools.append(close_attacks_menu)
        tools.append(run_from_current_battle)
        tools.append(toggle_auto_run_feat)

    pvp_agent = Agent(
        name="pvp_agent",
        model="gemini-2.5-flash",
        description=pvp_agent_description,
        instruction=pvp_agent_instructions,
        tools=tools,
        before_model_callback=[inject_world_state],
        after_tool_callback=[update_internal_worldstate],
    )

    return pvp_agent
