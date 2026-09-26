import os
import importlib
from utils import debug, warn
from error_handler import safe_execute
from plugin_api import PluginAPI


class PluginLoader:
    """
    Legacy-style plugin loader kept for compatibility.
    Loads plugins from /plugins and registers them using PluginAPI.
    This file is optional in the new architecture but maintained
    because your project includes it.
    """

    def __init__(self, controller):
        self.controller = controller
        self.loaded_plugins = {}

    # ---------------------------------------------------------
    # Load plugins
    # ---------------------------------------------------------
    def load(self):
        plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")

        if not os.path.isdir(plugin_dir):
            warn("[PLUGIN_LOADER] No plugins directory found.")
            return

        for filename in os.listdir(plugin_dir):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue

            module_name = filename[:-3]
            module_path = f"plugins.{module_name}"

            try:
                module = importlib.import_module(module_path)

                if hasattr(module, "register"):
                    api = PluginAPI(self.controller)
                    safe_execute(module.register, api)

                    self.loaded_plugins[module_name] = module
                    debug(f"[PLUGIN_LOADER] Registered plugin: {module_name}")

                else:
                    warn(f"[PLUGIN_LOADER] Plugin missing register(): {module_name}")

            except Exception as e:
                warn(f"[PLUGIN_LOADER] Failed to load {module_name}: {e}")

    # ---------------------------------------------------------
    # Reload plugins
    # ---------------------------------------------------------
    def reload(self):
        plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")

        for filename in os.listdir(plugin_dir):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue

            module_name = filename[:-3]
            module_path = f"plugins.{module_name}"

            try:
                if module_path in importlib.sys.modules:
                    del importlib.sys.modules[module_path]

                module = importlib.import_module(module_path)

                if hasattr(module, "register"):
                    api = PluginAPI(self.controller)
                    safe_execute(module.register, api)

                    self.loaded_plugins[module_name] = module
                    debug(f"[PLUGIN_LOADER] Reloaded plugin: {module_name}")

                else:
                    warn(f"[PLUGIN_LOADER] Plugin missing register(): {module_name}")

            except Exception as e:
                warn(f"[PLUGIN_LOADER] Failed to reload {module_name}: {e}")
