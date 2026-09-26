from .utils import debug


class Config:
    """
    Simple configuration store.
    Behaves like StateManager but intended for persistent or
    semi‑persistent settings that plugins and core systems read.
    """

    def __init__(self):
        self._config = {}

    # ---------------------------------------------------------
    # Set
    # ---------------------------------------------------------
    def set(self, key, value):
        debug(f"[CONFIG] Set {key} -> {value}")
        self._config[key] = value
        return value

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------
    def get(self, key, default=None):
        return self._config.get(key, default)

    # ---------------------------------------------------------
    # All
    # ---------------------------------------------------------
    def all(self):
        return dict(self._config)

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------
    def clear(self):
        debug("[CONFIG] Cleared")
        self._config.clear()
