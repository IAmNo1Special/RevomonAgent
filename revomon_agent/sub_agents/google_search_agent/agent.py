from google.adk.agents import Agent
from google.adk.tools import google_search

from .descriptions import google_search_agent_description
from .instructions import google_search_agent_instructions

def create_google_search_agent() -> Agent:
    return Agent(
        name="google_search_agent",
        model="gemini-2.5-flash",
        description=google_search_agent_description,
        instruction=google_search_agent_instructions,
        tools=[google_search],
    )
