from utils import debug
from error_handler import safe_execute


class ActionExecutor:
    """
    Executes named actions requested by plugins or core systems.
    Actions are simple callables registered at runtime.
    """

    def __init__(self):
        self._actions = {}

    # ---------------------------------------------------------
    # Register an action
    # ---------------------------------------------------------
    def register(self, name: str, handler):
        debug(f"[ACTIONS] Register action: {name}")
        self._actions[name] = handler

    # ---------------------------------------------------------
    # Unregister an action
    # ---------------------------------------------------------
    def unregister(self, name: str):
        if name in self._actions:
            debug(f"[ACTIONS] Unregister action: {name}")
            del self._actions[name]

    # ---------------------------------------------------------
    # Execute an action by name with args/kwargs
    # Returns the handler result or raises KeyError if missing
    # ---------------------------------------------------------
    def execute(self, name: str, *args, **kwargs):
        debug(f"[ACTIONS] Execute: {name} args={args} kwargs={kwargs}")
        handler = self._actions.get(name)
        if not handler:
            raise KeyError(f"Action not found: {name}")

        return safe_execute(handler, *args, **kwargs)

    # ---------------------------------------------------------
    # List registered actions
    # ---------------------------------------------------------
    def list(self):
        return list(self._actions.keys())
