from google.adk.tools.function_tool import FunctionTool

from revomon_agent.toolbox.tools import REVO_TOOLS
from .utils import get_mcp_server_script


class _McpConfig:
    def __init__(self):
        self.MCP_SERVER_SCRIPT = str(get_mcp_server_script(__file__))
        self.MCP_FUNCTION_TOOLS, self.MCP_TOOL_MAP = None, None
        self._create_function_tools(REVO_TOOLS)

    def _create_function_tools(self, functions) -> None:
        """
        Creates a list of FunctionTool objects from the given functions.

        Args:
            functions: A single function or a list of functions to convert

        Returns:
            A single FunctionTool if input is a single function, or a list of FunctionTools if input is a list
        """
        if not isinstance(functions, list):
            # Handle single function case
            functions = [functions]

        function_tools = []
        for func in functions:
            function_tool = FunctionTool(func)
            function_tools.append(function_tool)
            print(
                f"ADK FunctionTool '{function_tool.name}' initialized and ready to be exposed via MCP."
            )
        self.MCP_FUNCTION_TOOLS = function_tools

        tool_map = {tool.name: tool for tool in function_tools}
        self.MCP_TOOL_MAP = tool_map


mcp_config = _McpConfig()
