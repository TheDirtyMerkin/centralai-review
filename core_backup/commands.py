from .utils import debug
from .error_handler import safe_execute


class CommandRegistry:
    """
    Legacy command registry.
    Modern plugins use metadata-based routing in plugin_manager,
    but older modules still rely on this registry.
    """

    def __init__(self):
        self._commands = {}

    # ---------------------------------------------------------
    # Register
    # ---------------------------------------------------------
    def register(self, keyword, handler):
        debug(f"[COMMANDS] Register command: {keyword}")
        self._commands[keyword] = handler

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------
    def execute(self, keyword, *args):
        handler = self._commands.get(keyword)
        if not handler:
            return None
        return safe_execute(handler, *args)

    # ---------------------------------------------------------
    # List
    # ---------------------------------------------------------
    def list(self):
        return list(self._commands.keys())
