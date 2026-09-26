# CentralAI (Minimal Core)

CentralAI is a small, modular conversational engine intended as a learning and prototyping scaffold.  
It demonstrates a lightweight architecture for routing, plugins, memory, history, and simple action execution.

> **Not production-ready.** This repository is designed for experimentation, education, and local development.

## Features

- **Engine**: Preprocess → route → execute → generate response.
- **Plugin-friendly**: Simple plugin loader and plugin API for extending behavior.
- **State & Config**: In-memory stores for runtime state and configuration.
- **Memory & History**: Short-term conversational memory and timestamped history.
- **Action Executor**: Register and run named actions safely.
- **Error handling**: Centralized safe execution wrapper to prevent crashes.
- **Personality**: Legacy prefix/suffix system for response styling.
- **Settings**: `settings.json` for toggles and defaults.

## Quick start

1. Create a Python 3.10+ virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
