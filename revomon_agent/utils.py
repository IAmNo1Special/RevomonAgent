import json
from os import path as os_path

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.genai import types

from .configs.app import app_config
from .services.memory import memory_service
from .services.session import session_service


def get_mcp_server_script(file_path):
    return os_path.join(
        os_path.dirname(os_path.abspath(file_path)), "revomonauto_mcp_server.py"
    )


async def create_session_runner(root_agent: Agent):
    session = await session_service.create_session(
        app_name=app_config.APP_NAME,
        user_id=app_config.USER_ID,
        session_id=app_config.SESSION_ID,
        state={},
    )

    runner = Runner(
        app_name=app_config.APP_NAME,
        agent=root_agent,
        session_service=session_service,
        memory_service=memory_service,
    )

    return session, runner


async def call_agent_async(runner: Runner, query: str, image_bytes: bytes = None):
    """Sends the query to the agent and calls on_message with each response."""
    if image_bytes:
        content = types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=query),
                types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
            ],
        )
    else:
        content = types.Content(role="user", parts=[types.Part.from_text(text=query)])
    async for event in runner.run_async(
        user_id=app_config.USER_ID,
        session_id=app_config.SESSION_ID,
        new_message=content,
    ):
        author = event.author

        if not event.content:
            print(f"<<< [{author}][UNKNOWN EVENT TYPE][{event.type}]: {event}")
            return

        parts = event.content.parts

        for part in parts:
            if part.text:
                text = part.text
                # Truncate long text to 200 characters
                # if len(text) > 200:
                # text = text[:197] + "..."
                if event.is_final_response:
                    if "/*" in text:
                        continue
                    print(f"[User] <<< [{author}][FINAL RESPONSE]: {text}")
                else:
                    print(f"[User] <<< [{author}][RESPONSE]: {text}")
            if part.function_call:
                func_call = part.function_call
                print(f"[{author}][FUNCTION CALL] >>> [{func_call.name}]")
                # Truncate args if too long
                args = json.dumps(func_call.args)
                # if len(args) > 100:
                # args = args[:97] + "..."
                print(f"    ^^^ [ARGS]: {args}")
            if part.function_response:
                func_response = part.function_response
                print(f"[{author}] <<< [{func_response.name}][FUNCTION RESPONSE]")
                # Truncate response if too long
                response = json.dumps(func_response.response)
                # if len(response) > 100:
                # response = response[:97] + "..."
                print(f"    ^^^ [RESPONSE]: {response}")
            if part.inline_data:
                inline_data = part.inline_data
                print(f"[{author}][INLINE DATA] >>> [{inline_data.display_name}]")
                # Truncate data if too long
                data = json.dumps(inline_data.data)
                # if len(data) > 100:
                # data = data[:97] + "..."
                print(f"    ^^^ [DATA]: {data}")
            if part.thought_signature:
                thought_signature = part.thought_signature
                print(f"[{author}][THOUGHT SIGNATURE] >>> [{thought_signature}]")


async def main_loop():
    try:
        session, runner = await create_session_runner()
        while True:
            query = input(">>").strip()
            if query == "":
                continue
            if query:
                print(f"[User][QUERY] >>> [Tasha]: {query}")
                # revomon_app_controller._controller.capture_screenshot(fp=fp)
                # await call_agent_async(query, image_bytes=draw_grid_on_image(fp, grid_size=100))
                await call_agent_async(runner=runner, query=query)
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")
