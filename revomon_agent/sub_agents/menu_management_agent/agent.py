from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from ..clan_agent import create_clan_agent
from ..discussion_agent import create_discussion_agent
from ..friends_list_agent import create_friends_list_agent
from ..inventory_agent import create_inventory_agent
from ..main_menu_agent import create_main_menu_agent
from ..market_agent import create_market_agent
from ..revodex_agent import create_revodex_agent
from ..settings_agent import create_settings_agent
from ..wardrobe_agent import create_wardrobe_agent
from .descriptions import menu_management_agent_description
from .instructions import menu_management_agent_instructions

load_dotenv()


def create_menu_management_agent(use_mcp_tools: bool = False) -> Agent:
    clan_agent = create_clan_agent(use_mcp_tools)
    discussion_agent = create_discussion_agent(use_mcp_tools)
    friends_list_agent = create_friends_list_agent(use_mcp_tools)
    inventory_agent = create_inventory_agent(use_mcp_tools)
    main_menu_agent = create_main_menu_agent(use_mcp_tools)
    market_agent = create_market_agent(use_mcp_tools)
    revodex_agent = create_revodex_agent(use_mcp_tools)
    settings_agent = create_settings_agent(use_mcp_tools)
    wardrobe_agent = create_wardrobe_agent(use_mcp_tools)

    menu_management_agent = Agent(
        name="menu_management_agent",
        model="gemini-2.5-flash",
        description=menu_management_agent_description,
        instruction=menu_management_agent_instructions,
        tools=[
            AgentTool(agent=clan_agent),
            AgentTool(agent=discussion_agent),
            AgentTool(agent=friends_list_agent),
            AgentTool(agent=inventory_agent),
            AgentTool(agent=main_menu_agent),
            AgentTool(agent=market_agent),
            AgentTool(agent=revodex_agent),
            AgentTool(agent=settings_agent),
            AgentTool(agent=wardrobe_agent),
        ],
    )

    return menu_management_agent
