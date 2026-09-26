"""
core/commands.py

Legacy command registry kept for backward compatibility.
Provides a simple mapping of keyword -> handler with safe execution.
"""

from typing import Any, Callable, Dict, List, Optional

# Import debug and safe_execute defensively to avoid circular import issues.
try:
    from .utils import debug  # type: ignore
except Exception:
    def debug(msg: str) -> None:
        print(msg)


try:
    from .error_handler import safe_execute  # type: ignore
except Exception:
    # Fallback: a minimal safe_execute that simply calls the function.
    def safe_execute(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Optional[Any]:
        try:
            return func(*args, **kwargs)
        except Exception:
            return None


class CommandRegistry:
    """
    Simple command registry.

    - register(keyword, handler): register a handler callable for a keyword
    - execute(keyword, *args): execute the handler safely and return its result
    - list_commands(): return a list of registered keywords
    """

    def __init__(self) -> None:
        self._commands: Dict[str, Callable[..., Any]] = {}

    # ---------------------------------------------------------
    # Register
    # ---------------------------------------------------------
    def register(self, keyword: str, handler: Callable[..., Any]) -> None:
        """Register a command handler for the given keyword."""
        debug(f"[COMMANDS] Register command: {keyword}")
        self._commands[keyword] = handler

    # ---------------------------------------------------------
    # Execute
    # ---------------------------------------------------------
    def execute(self, keyword: str, *args: Any, **kwargs: Any) -> Optional[Any]:
        """
        Execute the handler registered for `keyword` using safe_execute.
        Returns the handler's result, or None if no handler is registered or it fails.
        """
        handler = self._commands.get(keyword)
        if not handler:
            debug(f"[COMMANDS] No handler for: {keyword}")
            return None
        return safe_execute(handler, *args, **kwargs)

    # ---------------------------------------------------------
    # List
    # ---------------------------------------------------------
    def list_commands(self) -> List[str]:
        """Return a list of registered command keywords."""
        return list(self._commands.keys())

    # Backwards-compatible alias named `list`
    list = list_commands  # type: ignore

