from utils import debug
from error_handler import safe_execute


class PluginAPI:
    """
    API exposed to plugins.
    Allows controlled interaction with CentralAI internals.
    """

    def __init__(self, controller):
        self.controller = controller

    # ---------------------------------------------------------
    # State
    # ---------------------------------------------------------
    def set_state(self, key, value):
        debug(f"[PLUGIN_API] set_state {key} -> {value}")
        return self.controller.state.set(key, value)

    def get_state(self, key, default=None):
        return self.controller.state.get(key, default)

    # ---------------------------------------------------------
    # Memory
    # ---------------------------------------------------------
    def remember(self, item):
        debug(f"[PLUGIN_API] remember {item}")
        return self.controller.memory.remember(item)

    def recall(self):
        return self.controller.memory.recall()

    # ---------------------------------------------------------
    # Config
    # ---------------------------------------------------------
    def set_config(self, key, value):
        debug(f"[PLUGIN_API] set_config {key} -> {value}")
        return self.controller.config.set(key, value)

    def get_config(self, key, default=None):
        return self.controller.config.get(key, default)

    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------
    def on(self, event_name, handler):
        debug(f"[PLUGIN_API] register event handler for {event_name}")
        self.controller.events.on(event_name, handler)

    def emit(self, event_name, *args, **kwargs):
        debug(f"[PLUGIN_API] emit event {event_name}")
        return self.controller.events.emit(event_name, *args, **kwargs)

    # ---------------------------------------------------------
    # Commands
    # ---------------------------------------------------------
    def register_command(self, keyword, handler):
        """
        Legacy command registration for plugins using plugin_loader.
        plugin_manager handles modern metadata‑based commands.
        """
        debug(f"[PLUGIN_API] register command {keyword}")
        self.controller.router.routes[keyword] = handler

    # ---------------------------------------------------------
    # Safe execution helper
    # ---------------------------------------------------------
    def safe(self, func, *args, **kwargs):
        return safe_execute(func, *args, **kwargs)
