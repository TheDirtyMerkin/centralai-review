"""
core/error_handler.py

Safe execution wrapper for plugin and handler calls. Handlers may raise
exceptions; safe_execute will log the traceback and return None so a single
failing handler does not crash the host application.
"""

from typing import Any, Callable, Optional
import traceback

# Import debug defensively to avoid circular import problems during module import.
try:
    from .utils import debug  # type: ignore
except Exception:
    def debug(msg: str) -> None:
        # Fallback simple logger if utils.debug is unavailable.
        print(msg)


class HandlerError(Exception):
    """Raised when a handler fails in a way the system should surface."""


def safe_execute(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Optional[Any]:
    """
    Execute a callable and capture exceptions.

    Returns the callable's result on success, or None on failure.
    Exceptions are logged via debug; handler/plugin errors are swallowed
    (returning None) to avoid crashing the host. If callers need a different
    behavior (for example, to surface critical failures), they should catch
    exceptions themselves or wrap the handler accordingly.
    """
    try:
        return func(*args, **kwargs)
    except Exception as ex:
        tb = traceback.format_exc()
        try:
            debug(
                f"[ERROR_HANDLER] Exception in {getattr(func, '__name__', repr(func))}: {ex}\n{tb}"
            )
        except Exception:
            # As a last resort, print to stdout so the error is visible.
            print(f"[ERROR_HANDLER] Exception: {ex}\n{tb}")
        # For plugin/handler errors we swallow and return None to avoid crashing the host.
        return None

