from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest
from google.adk.tools.tool_context import ToolContext
from google.genai import types

from ..configs.app import app_config


def update_internal_worldstate(
    tool=None,
    args=None,
    tool_context: ToolContext = None,
    callback_context: CallbackContext = None,
    tool_response=None,
    llm_request: LlmRequest = None,
) -> None:
    """
    Updates the current world state in the agents state context.

    Args:
        tool: The google adk provided tool object.
        args: The google adk provided args object.
        tool_response: The google adk provided tool_response object.
        tool_context: The google adk provided ToolContext object.

    Returns:
        None
    """
    ctx = tool_context if tool_context else callback_context
    previous_world_state = ctx.state.get("user:current_world_state", None)
    ctx.state["user:previous_world_state"] = previous_world_state
    current_world_state = app_config.REVO_APP_CONTROLLER.get_current_state()
    ctx.state["user:current_world_state"] = current_world_state
    return None


def inject_world_state(
    tool=None,
    args=None,
    tool_context: ToolContext = None,
    callback_context: CallbackContext = None,
    tool_response=None,
    llm_request: LlmRequest = None,
) -> None:
    """
    Injects the world state into the llm request.

    Args:
        callback_context: The google adk provided CallbackContext object.
        llm_request: The google adk provided LlmRequest object.
    Returns:
        None
    """
    update_internal_worldstate(
        callback_context=callback_context,
        llm_request=llm_request,
    )
    previous_world_state = callback_context.state.get("user:previous_world_state", None)
    current_world_state = callback_context.state.get("user:current_world_state", None)
    llm_request.contents[-1].parts.append(
        types.Part.from_text(text=f"Previous World State: {previous_world_state}")
    )
    llm_request.contents[-1].parts.append(
        types.Part.from_text(text=f"Current World State: {current_world_state}")
    )
    return None
