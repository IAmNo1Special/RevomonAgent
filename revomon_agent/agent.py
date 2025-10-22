from os import path as os_path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.planners import PlanReActPlanner
from google.adk.tools.agent_tool import AgentTool

from .callbacks import inject_world_state
from .descriptions import revoagent_description
from .instructions import revoagent_instructions
from .sub_agents import (
    create_app_launcher_agent,
    create_google_search_agent,
    create_menu_management_agent,
    create_pvp_agent,
    create_tv_agent,
)

load_dotenv()


def create_root_agent(use_mcp_tools: bool = False) -> Agent:
    app_launcher_agent = create_app_launcher_agent(use_mcp_tools)
    google_search_agent = create_google_search_agent()
    menu_management_agent = create_menu_management_agent(use_mcp_tools)
    pvp_agent = create_pvp_agent(use_mcp_tools)
    tv_agent = create_tv_agent(use_mcp_tools)

    root_agent = Agent(
        name="RevomonAutoAgent",
        model="gemini-2.5-pro",
        description=revoagent_description,
        instruction=revoagent_instructions,
        tools=[
            AgentTool(agent=app_launcher_agent),
            AgentTool(agent=google_search_agent),
            AgentTool(agent=menu_management_agent),
            AgentTool(agent=pvp_agent),
            AgentTool(agent=tv_agent),
        ],
        planner=PlanReActPlanner(),
        before_model_callback=[inject_world_state],
    )

    return root_agent


root_agent = create_root_agent()
