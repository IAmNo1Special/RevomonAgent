# RevomonAgent

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![BlueStacks](https://img.shields.io/badge/Platform-BlueStacks-orange.svg)](https://www.bluestacks.com)

**An AI-powered automation assistant for the Revomon game, built with Google's Android Development Kit (ADK) and designed to run on BlueStacks emulator.**

RevomonAgent is a sophisticated open-source AI assistant that automates gameplay in the Android game Revomon. Using Google's ADK framework with the Gemini 2.5 Pro model for the main agent (and Flash for sub-agents), it provides intelligent automation for PvP battles, menu navigation, inventory management, and more. The system is built on a three-layer architecture using custom BluePyll ADB automation and the revomonauto game controller.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#install-revomonagent)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## Features

### 🤖 AI-Powered Game Automation

- **5 Main Sub-Agents**: App launcher, Google search, menu management, PvP, and TV agents
- **Intelligent Planning**: Uses Google's PlanReActPlanner for complex multi-step task execution
- **Conversational Interface**: Natural language processing with context-aware responses
- **Flexible AI Models**: Main agent uses Gemini 2.5 Pro, sub-agents use Flash (configurable)

### 🎮 Complete Game Control

- **App Management**: Launch, close, and manage Revomon app lifecycle
- **PvP Automation**: Queue management, battle controls, and attack strategies
- **Menu Navigation**: Seamless navigation through all game menus and interfaces
- **Inventory & Market**: Automated item management and marketplace interactions
- **TV System**: Creature searching and selection via in-game TV

### 🔧 Technical Excellence

- **State Management**: Real-time world state tracking and synchronization
- **MCP Integration**: Model Context Protocol server for external tool access
- **Error Handling**: Robust error recovery and status reporting
- **Logging**: Comprehensive logging for debugging and monitoring

## Architecture

RevomonAgent uses a sophisticated three-layer architecture:

```text
┌─────────────────┐
│  RevomonAgent   │  ← Google ADK Agent System
│                 │     5 Main Sub-Agents, MCP Server
├─────────────────┤
│   revomonauto   │  ← Game-Specific Controller
│                 │     RevoAppController
├─────────────────┤
│    BluePyll     │  ← BlueStacks ADB Automation
│                 │     UI Control, Image Recognition
└─────────────────┘
         ↓
┌─────────────────┐
│   BlueStacks    │  ← Android Emulator
│   Emulator      │     Running Revomon Game
└─────────────────┘
```

**Platform Requirements:**

- BlueStacks Android emulator (latest version recommended)
- Revomon game installed and configured in BlueStacks

## Project Structure

```text
revomonagent/
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore patterns
├── .python-version       # Python version specification
├── pyproject.toml        # Project configuration and dependencies
├── README.md             # This file
├── uv.lock              # UV package manager lock file
└── revomon_agent/        # Main source directory
    ├── __init__.py       # Module initialization
    ├── agent.py          # Root agent implementation
    ├── callbacks/        # ADK callback handlers
    │   ├── __init__.py
    │   └── callbacks.py
    ├── configs/          # Shared configurations
    │   └── app.py
    ├── descriptions.py   # Root agent descriptions
    ├── instructions.py   # Root agent instructions
    ├── logs/             # Log files directory
    ├── revomonagent_mcp/ # MCP server directory
    │   ├── __init__.py
    │   ├── config.py
    │   ├── server.py
    │   └── utils.py
    ├── services/         # Services directory
    │   ├── __init__.py
    │   ├── ears.py   # Not Implemented
    │   ├── memory.py
    │   ├── session.py
    │   └── voice.py  # Not Implemented
    ├── sub_agents/       # Specialized sub-agents
    │   ├── __init__.py
    │   ├── app_launcher_agent/
    │   ├── clan_agent/
    │   ├── discussion_agent/
    │   ├── friends_list_agent/
    │   ├── google_search_agent/
    │   ├── inventory_agent/
    │   ├── main_menu_agent/
    │   ├── market_agent/
    │   ├── menu_management_agent/
    │   ├── pvp_agent/
    │   ├── revodex_agent/
    │   ├── settings_agent/
    │   ├── tv_agent/
    │   └── wardrobe_agent/
    ├── toolbox/          # Game interaction tools
    │   └── tools.py
    └── utils/            # Shared utility modules
        ├── __init__.py
        └── utils.py
```

### Prerequisites

1. **Install BlueStacks**

   ```bash
   # Download and install BlueStacks from:
   # https://www.bluestacks.com/download.html
   # Ensure Revomon is installed within BlueStacks
   ```

2. **Install Python 3.13+**

   ```bash
   # Download from:
   # https://www.python.org/downloads/
   ```

3. **Install uv (Recommended Package Manager)**

   ```bash
   pip install uv
   ```

### Install RevomonAgent

```bash
# Clone the repository
git clone https://github.com/IAmNo1Special/RevomonAgent.git
cd revomonagent

# Install in development mode
uv sync --dev

# Set up environment variables
cp .env.example .env
# Edit .env file with your configuration
```

### Configuration

Edit the now named `.env` file in the project root:

```env
# If using Gemini via Google AI Studio
GOOGLE_GENAI_USE_VERTEXAI=False
GOOGLE_API_KEY=<YOUR_GOOGLE_GEMINI_API_KEY>
```

Update GOOGLE_API_KEY with your Google Gemini API key.

## Quick Start

```python
from revomon_agent import create_root_agent

# Create and initialize the AI agent
agent = create_root_agent()

# Example: Start a PvP battle
response = agent.run("Start a PvP battle and use my best team")

# Example: Navigate to inventory
response = agent.run("Open the main menu and go to my inventory")

# Example: Search for a specific Revomon
response = agent.run("Search the TV for Pikachu and show me the results")
```

## How It Works

This section provides a technical overview of RevomonAgent's architecture and implementation to help developers understand the codebase.

### Agent Architecture

**Root Agent (`revomon_agent/agent.py`):**

```python
from revomon_agent import create_root_agent

# Creates the main AI agent with 5 integrated sub-agents
agent = create_root_agent(use_mcp_tools=False)  # Standard mode
# agent = create_root_agent(use_mcp_tools=True)  # MCP mode
```

**Model Configuration:**

- Main agent uses Gemini 2.5 Pro for complex planning and orchestration
- Sub-agents use Gemini 2.5 Flash for faster, cost-effective responses
- Models can be configured in the agent creation functions

**Agent Hierarchy:**

- **Root Agent**: Orchestrates all game automation with PlanReActPlanner
- **5 Main Sub-Agents**: App launcher, Google search, menu management, PvP, TV
- **Menu Management**: Contains 9 additional specialized agents for specific menus
- **Toolbox**: 30+ low-level functions exposed as ADK FunctionTools

### Tool System

**Standard Mode:**

- Tools are wrapped as `FunctionTool` objects
- Direct function calls with immediate execution
- Lower latency, simpler debugging

**MCP Mode:**

- Tools exposed via external MCP server
- `use_mcp_tools=True` enables automatic server management
- Google ADK handles server lifecycle (start/stop)

**Tool Categories:**

- **App Control**: `open_revomon_app()`, `close_revomon_app()`, `start_revomon_game()`
- **Game Actions**: `enter_revomon_pvp_queue()`, `open_main_menu()`, `open_wardrobe()`
- **TV System**: `tv_search_for_revomon()`, `tv_select_slot()`
- **Combat**: `run_from_current_battle()`, `toggle_auto_run_feat()`

### Key Components

**1. Toolbox (`revomon_agent/toolbox/tools.py`)**

- Contains 30+ game interaction functions
- All functions follow the pattern: `function() -> dict` with `{"success": bool, "message": str}`
- Uses `app_config.REVO_APP_CONTROLLER` for BlueStacks integration

**2. Agent Instructions (`revomon_agent/instructions.py`)**

- Defines system prompts and behavior guidelines
- Context-aware responses and error handling
- Natural language processing capabilities

**3. State Management (`revomon_agent/callbacks/callbacks.py`)**

- `inject_world_state()` callback provides real-time game state
- Automatic state synchronization before each AI decision
- World state tracking for informed actions

**4. MCP Integration (`revomon_agent/revomonagent_mcp/`)**

- Automatic server management when `use_mcp_tools=True`
- Exposes all toolbox functions via stdio protocol
- External tool access for integrations

### Development Workflow

**For Contributors:**

```bash
# 1. Clone and setup
git clone https://github.com/IAmNo1Special/RevomonAgent.git
cd RevomonAgent
uv sync --dev

# 2. Run tests
uv run pytest

# 3. Add new features
# - Add functions to toolbox/tools.py
# - Create new agents in sub_agents/
# - Update agent.py to integrate new agents
# - Update instructions.py for new capabilities
```

**Adding New Tools:**

1. Implement function in `toolbox/tools.py`
2. Follow naming: `function_name() -> dict`
3. Add error handling with try/except
4. Return `{"success": True/False, "message": "..."}`
5. Function automatically available in both modes

**Adding New Agents:**

1. Create new directory in `sub_agents/`
2. Implement `create_*_agent()` function
3. Add to `agent.py` imports and root agent
4. Update MCP config if needed

### Integration Points

**BluePyll Layer:**

- Low-level ADB automation for BlueStacks
- UI element detection and interaction
- Image recognition capabilities

**RevomonAuto Layer:**

- Game-specific automation built on BluePyll
- `RevoAppController` handles Revomon game logic
- State management and high-level game interactions

## Contributing

We welcome contributions! Please see our contribution guidelines below.

### Development Setup

```bash
# Clone for development
git clone https://github.com/IAmNo1Special/RevomonAgent.git
cd RevomonAgent

# Install in development mode (creates venv automatically)
uv sync --dev

# Run tests
uv run pytest

# Run linting
uv run ruff check .
uv run ruff format --check .
```

### Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html)
- Maximum line length: 88 characters
- Use `ruff` for linting and `black` for formatting

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure all tests pass: `uv run pytest`
5. Run linting: `uv run ruff check . && uv run ruff format --check .`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/IAmNo1Special/RevomonAgent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/IAmNo1Special/RevomonAgent/discussions)

### Common Issues

**BlueStacks Connection Issues:**

- Ensure BlueStacks is running before starting RevomonAgent
- Check ADB port configuration in `.env` file
- Verify Revomon is installed in BlueStacks

**Agent Not Responding:**

- Check Google API key configuration
- Verify all dependencies are installed: `uv sync`
- Check logs in `revomon_agent/logs/`

**Game State Issues:**

- Restart the Revomon app within BlueStacks
- Clear BlueStacks cache if experiencing persistent issues

## License

This project is licensed under the MIT License.

---

## Made with ❤️ for the Revomon community

*RevomonAgent was created to enhance the Revomon gameplay experience through intelligent automation. Please use responsibly and in accordance with Revomon's terms of service.*
