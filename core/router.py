"""
core/router.py

Command router for CentralAI. Routes text commands to the legacy command
registry or built-in handlers. Plugins may intercept before this router.
"""

from typing import Optional, List

from .utils import debug
from .commands import CommandRegistry


class CentralAIRouter:
    """
    Core command router.

    Plugins get first chance via a plugin manager (not shown here). This router
    handles legacy commands via an internal CommandRegistry and a few built-in
    handlers for state, memory, and config operations.
    """

    def __init__(self, controller) -> None:
        self.controller = controller
        self.routes = {}
        self.commands = CommandRegistry()

        # Register built-in commands
        self._register_core()

    # ---------------------------------------------------------
    # Core commands
    # ---------------------------------------------------------
    def _register_core(self) -> None:
        self.commands.register("state", self._cmd_state)
        self.commands.register("remember", self._cmd_remember)
        self.commands.register("recall", self._cmd_recall)
        self.commands.register("config", self._cmd_config)

    # ---------------------------------------------------------
    # Route
    # ---------------------------------------------------------
    def route(self, text: str) -> Optional[str]:
        """Route a single line of text to a command handler."""
        debug(f"[ROUTER] Routing: {text}")

        parts: List[str] = (text or "").split()
        if not parts:
            return None

        keyword = parts[0]
        args = parts[1:]

        # Legacy command registry
        result = self.commands.execute(keyword, *args)
        if result is not None:
            return result

        # No match
        return f"Unknown command: {keyword}"

    # ---------------------------------------------------------
    # Built-in command handlers
    # ---------------------------------------------------------
    def _cmd_state(self, *args):
        if len(args) == 0:
            return self.controller.state.all()

        if len(args) == 1:
            return self.controller.state.get(args[0])

        key, value = args[0], " ".join(args[1:])
        return self.controller.state.set(key, value)

    def _cmd_remember(self, *args):
        item = " ".join(args)
        return self.controller.memory.remember(item)

    def _cmd_recall(self, *args):
        return self.controller.memory.recall()

    def _cmd_config(self, *args):
        if len(args) == 0:
            return self.controller.config.all()

        if len(args) == 1:
            return self.controller.config.get(args[0])

        key, value = args[0], " ".join(args[1:])
        return self.controller.config.set(key, value)
