from pathlib import Path

def get_mcp_server_script(file_path):
    return (Path(file_path).parent / "server.py").resolve()