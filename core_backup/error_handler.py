import traceback
from .utils import debug


class HandlerError(Exception):
    """Raised when a handler fails in a way the system should surface."""


def safe_execute(func, *args, **kwargs):
    """
    Execute a callable and capture exceptions.
    Returns the callable's result on success, or None on failure.
    Exceptions are logged via debug; critical failures raise HandlerError.
    """
    try:
        return func(*args, **kwargs)
    except Exception as ex:
        tb = traceback.format_exc()
        debug(f"[ERROR_HANDLER] Exception in {getattr(func, '__name__', repr(func))}: {ex}\n{tb}")
        # For plugin/handler errors we swallow and return None to avoid crashing the host.
        return None
