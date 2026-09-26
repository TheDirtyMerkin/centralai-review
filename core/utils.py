"""
core/utils.py

Small logging helpers used across the project. Kept intentionally simple so
they can be used in environments without the standard logging module.
"""

from typing import Any
import datetime


def timestamp() -> str:
    """Return a human-readable timestamp for log messages."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _log(level: str, msg: Any) -> None:
    """Internal helper to print a single-line log message."""
    try:
        text = str(msg)
    except Exception:
        text = "<unprintable message>"
    print(f"[{level} {timestamp()}] {text}", flush=True)


def debug(msg: Any) -> None:
    """Debug-level message."""
    _log("DEBUG", msg)


def info(msg: Any) -> None:
    """Informational message."""
    _log("INFO", msg)


def warn(msg: Any) -> None:
    """Warning message."""
    _log("WARN", msg)


def error(msg: Any) -> None:
    """Error message."""
    _log("ERROR", msg)
