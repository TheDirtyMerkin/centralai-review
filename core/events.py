"""
core/events.py

Simple event bus used by core systems and plugins. Handlers are executed
safely via the project's error handler wrapper.
"""

from typing import Any, Callable, Dict, List

from .utils import debug
from .error_handler import safe_execute


class EventManager:
    """
    Lightweight event manager.

    - Use on(event_name, handler) to register handlers.
    - Use emit(event_name, *args, **kwargs) to call handlers.
    Handlers are executed through safe_execute to prevent a single failing
    handler from breaking the emitter.
    """

    def __init__(self) -> None:
        self._handlers: Dict[str, List[Callable[..., Any]]] = {}

    # ---------------------------------------------------------
    # Register handler
    # ---------------------------------------------------------
    def on(self, event_name: str, handler: Callable[..., Any]) -> None:
        debug(f"[EVENTS] Register handler for {event_name}")
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)

    # ---------------------------------------------------------
    # Emit event
    # ---------------------------------------------------------
    def emit(self, event_name: str, *args: Any, **kwargs: Any) -> List[Any]:
        debug(f"[EVENTS] Emit: {event_name}")

        handlers = self._handlers.get(event_name, [])
        results: List[Any] = []

        for handler in handlers:
            result = safe_execute(handler, *args, **kwargs)
            results.append(result)

        return results
