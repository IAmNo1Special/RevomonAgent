from google.adk.tools.tool_context import ToolContext

from revomon_agent.configs.app import app_config


def tap_position(x: int, y: int) -> dict:
    """
    Tap at a given position on the screen.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.shell(f"input tap {x} {y}")
        return {"success": True, "message": f"Tapped at position: x:{x}, y:{y}"}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to tap at position: x:{x}, y:{y}: {e}",
        }


def open_revomon_app() -> dict:
    """
    Open the Revomon app using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_revomon_app()
        return {"success": True, "message": "Revomon app opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to open the Revomon app: {e}",
        }


def close_revomon_app() -> dict:
    """
    Close the Revomon app using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_revomon_app()
        return {"success": True, "message": "Revomon app closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to close the Revomon app: {e}",
        }


def start_revomon_game() -> dict:
    """
    Start the Revomon game using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.start_game()
        return {"success": True, "message": "Game started successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to start the game: {e}",
        }


def log_in_revomon() -> dict:
    """
    Log in to the Revomon game using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.log_in()
        return {"success": True, "message": "Logged in successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to log in: {e}",
        }


def enter_revomon_pvp_queue() -> dict:
    """
    Enter the PVP queue in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.enter_pvp_queue()
        return {"success": True, "message": "Entered the PVP queue successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to enter the PVP queue: {e}",
        }


def exit_revomon_pvp_queue() -> dict:
    """
    Exit the PVP queue in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.exit_pvp_queue()
        return {"success": True, "message": "Exited the PVP queue successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to exit the PVP queue: {e}",
        }


def open_attacks_menu() -> dict:
    """
    Open the attacks menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_attacks_menu()
        return {"success": True, "message": "Opened the attacks menu successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to open the attacks menu: {e}",
        }


def close_attacks_menu() -> dict:
    """
    Close the attacks menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_attacks_menu()
        return {"success": True, "message": "Closed the attacks menu successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to close the attacks menu: {e}",
        }


def run_from_current_battle() -> dict:
    """
    Run from the current battle in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """

    try:
        app_config.REVO_APP_CONTROLLER.run_from_battle()
        return {"success": True, "message": "Ran from the current battle successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to run from the current battle: {e}",
        }


def toggle_auto_run_feat() -> dict:
    """
    Toggle the auto-run feature in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.toggle_auto_run()
        return {"success": True, "message": "Auto-run feature toggled successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while toggle the auto-run feature: {e}",
        }


def open_main_menu() -> dict:
    """
    Open the main menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_main_menu()
        return {"success": True, "message": "Main menu opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the main menu: {e}",
        }


def close_main_menu() -> dict:
    """
    Close the main menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_main_menu()
        return {"success": True, "message": "Main menu closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the main menu: {e}",
        }


def open_wardrobe() -> dict:
    """
    Open the wardrobe in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_wardrobe()
        return {"success": True, "message": "Wardrobe opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the wardrobe: {e}",
        }


def close_wardrobe() -> dict:
    """
    Close the wardrobe interface.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_wardrobe()
        return {"success": True, "message": "Wardrobe closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the wardrobe: {e}",
        }


def recall_revomon() -> dict:
    """
    Recalls the Revomon monster currently following you in the overworld.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.recall_revomon()
        return {"success": True, "message": "Revomon recalled successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while recalling the Revomon: {e}",
        }


def open_friends_list() -> dict:
    """
    Opens the Revomon friends list interface.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_friends_list()
        return {"success": True, "message": "Friends list opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the friends list: {e}",
        }


def close_friends_list() -> dict:
    """
    Closes the friends list interface.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_friends_list()
        return {"success": True, "message": "Friends list closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the friends list: {e}",
        }


def open_settings() -> dict:
    """
    Open the settings in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_settings()
        return {"success": True, "message": "Settings opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the settings: {e}",
        }


def close_settings() -> dict:
    """
    Close the settings in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_settings()
        return {"success": True, "message": "Settings closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the settings: {e}",
        }


def open_revodex() -> dict:
    """
    Open the revodex in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_revodex()
        return {"success": True, "message": "Revodex opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the revodex: {e}",
        }


def close_revodex() -> dict:
    """
    Close the revodex in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_revodex()
        return {"success": True, "message": "Revodex closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the revodex: {e}",
        }


def open_market() -> dict:
    """
    Open the market in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """

    try:
        app_config.REVO_APP_CONTROLLER.open_market()
        return {"success": True, "message": "Market opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the market: {e}",
        }


def close_market() -> dict:
    """
    Close the market in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_market()
        return {"success": True, "message": "Market closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to close the market: {e}",
        }


def open_discussion() -> dict:
    """
    Open the discussion menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """

    try:
        app_config.REVO_APP_CONTROLLER.open_discussion()
        return {"success": True, "message": "Discussion opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the discussion: {e}",
        }


def close_discussion() -> dict:
    """
    Close the discussion menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_discussion()
        return {"success": True, "message": "Discussion closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to close the discussion: {e}",
        }


def open_clan_menu() -> dict:
    """
    Open the clan menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """

    try:
        app_config.REVO_APP_CONTROLLER.open_clan()
        return {"success": True, "message": "Clan menu opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the clan menu: {e}",
        }


def close_clan_menu() -> dict:
    """
    Close the clan menu in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_clan()
        return {"success": True, "message": "Clan menu closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to close the clan menu: {e}",
        }


def open_bag() -> dict:
    """
    Open the bag in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_available_bag()
        return {"success": True, "message": "Bag opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the bag: {e}",
        }


def close_bag() -> dict:
    """
    Close the bag in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_available_bag()
        return {"success": True, "message": "Bag closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the menu bag: {e}",
        }


def open_tv() -> dict:
    """
    Open the TV in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.open_tv()
        return {"success": True, "message": "TV opened successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while opening the TV: {e}",
        }


def close_tv() -> dict:
    """
    Closes the TV in Revomon using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.close_tv()
        return {"success": True, "message": "TV closed successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while closing the TV: {e}",
        }


def tv_search_for_revomon(revomon_name: str) -> dict:
    """
    Searches the TV for all revomon with the provided name in Revomon using the provided controller.

    Args:
        revomon_name (str): The name of the revomon you want to search for in the TV

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.tv_search_for_revomon(revomon_name=revomon_name)
        return {"success": True, "message": "TV search for revomon successful."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to search the tv for {revomon_name} the game: {e}",
        }


def tv_select_slot(slot_number: int) -> dict:
    """
    Select a specific slot between 1 and 36 in the TV in Revomon using the provided controller.

    Args:
        slot_number (int): The number of the slot you want to select in the TV

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.select_tv_slot(slot_number)
        return {"success": True, "message": "TV slot selected successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while trying to select tv slot # {slot_number}: {e}",
        }


def quit_game() -> dict:
    """
    Quit the Revomon game using the provided controller.

    Returns:
        dict: A dictionary containing a success status and message
    """
    try:
        app_config.REVO_APP_CONTROLLER.quit_game()
        return {"success": True, "message": "Game quit successfully."}
    except Exception as e:
        return {
            "success": False,
            "message": f"There was an error while quitting the game: {e}",
        }


def get_revo_tools() -> list:
    """
    Get a list of all tools available in the RevomonAgent toolbox.

    This function returns a list of all tools available in the RevomonAgent toolbox.
    The list contains all functions defined in the agents/tools/toolbox.py module.

    Returns:
        list: A list of all tools available in the RevomonAgent toolbox
    """
    revo_tools: list = []
    for tool in globals().values():
        if (
            callable(tool)
            and type(tool).__name__ == "function"
            and tool.__name__ != "get_revo_tools"
        ):
            revo_tools.append(tool)
    return revo_tools


REVO_TOOLS = get_revo_tools()
