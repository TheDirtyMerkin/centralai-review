"""
core/events_listener.py

Legacy event listener wrapper. Kept for backward compatibility with older
modules that expect a simple listener interface. Internally delegates to the
project's safe_execute wrapper so individual listener failures do not break
the emitter.
"""

from typing import Any, Callable, Dict, List

from .utils import debug
from .error_handler import safe_execute


class EventListener:
    """
    Legacy event listener system.

    Use:
      listener = EventListener(controller)
      listener.on("some_event", handler)
      listener.emit("some_event", arg1, kw=val)
    """

    def __init__(self, controller) -> None:
        self.controller = controller
        self._listeners: Dict[str, List[Callable[..., Any]]] = {}

    # ---------------------------------------------------------
    # Register listener
    # ---------------------------------------------------------
    def on(self, event_name: str, handler: Callable[..., Any]) -> None:
        debug(f"[EVENT_LISTENER] Register listener for {event_name}")
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(handler)

    # ---------------------------------------------------------
    # Emit event
    # ---------------------------------------------------------
    def emit(self, event_name: str, *args: Any, **kwargs: Any) -> List[Any]:
        debug(f"[EVENT_LISTENER] Emit: {event_name}")

        handlers = self._listeners.get(event_name, [])
        results: List[Any] = []

        for handler in handlers:
            result = safe_execute(handler, *args, **kwargs)
            results.append(result)

        return results
