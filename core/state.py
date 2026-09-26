"""
core/state.py

Simple key/value state store.
Plugins and core systems can read/write state.
"""

from typing import Any, Dict, Optional


class StateManager:
    """
    Simple key/value state store.

    Public methods:
    - set(key, value) -> Any: store a value and return it
    - get(key, default=None) -> Any: retrieve a value or default
    - all() -> Dict[str, Any]: return a shallow copy of all state
    - clear() -> None: clear all stored state
    """

    def __init__(self) -> None:
        self._state: Dict[str, Any] = {}

    # ---------------------------------------------------------
    # Set
    # ---------------------------------------------------------
    def set(self, key: str, value: Any) -> Any:
        """Set a key to value and return the value."""
        debug_msg = f"[STATE] Set {key} -> {value}"
        try:
            # Import debug lazily to avoid circular imports at module import time
            from .utils import debug  # type: ignore
            debug(debug_msg)
        except Exception:
            # If debug is unavailable, fail silently to avoid breaking callers
            pass

        self._state[key] = value
        return value

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------
    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get a value by key, returning default if not present."""
        return self._state.get(key, default)

    # ---------------------------------------------------------
    # All
    # ---------------------------------------------------------
    def all(self) -> Dict[str, Any]:
        """Return a shallow copy of the internal state dictionary."""
        return dict(self._state)

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------
    def clear(self) -> None:
        """Clear all stored state."""
        try:
            from .utils import debug  # type: ignore
            debug("[STATE] Cleared")
        except Exception:
            pass
        self._state.clear()
