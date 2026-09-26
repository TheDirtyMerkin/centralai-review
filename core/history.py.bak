from datetime import datetime
from utils import debug


class HistoryManager:
    """
    Conversation history store.
    Records timestamped entries for inputs and outputs.
    """

    def __init__(self, max_items: int = 1000):
        self._entries = []
        self._max = max_items

    # ---------------------------------------------------------
    # Add an entry
    # entry: dict with keys 'role' ('user'|'assistant'|'system'), 'text', optional 'meta'
    # ---------------------------------------------------------
    def add(self, entry: dict):
        if not isinstance(entry, dict):
            return None

        entry_copy = dict(entry)
        entry_copy.setdefault("role", "user")
        entry_copy.setdefault("text", "")
        entry_copy.setdefault("meta", {})
        entry_copy["timestamp"] = datetime.utcnow().isoformat() + "Z"

        debug(f"[HISTORY] Add entry: {entry_copy.get('role')} {entry_copy.get('text')}")
        self._entries.append(entry_copy)

        if len(self._entries) > self._max:
            self._entries = self._entries[-self._max :]

        return entry_copy

    # ---------------------------------------------------------
    # Get recent entries
    # ---------------------------------------------------------
    def recent(self, count: int = 10):
        return list(self._entries[-count:])

    # ---------------------------------------------------------
    # Get all entries
    # ---------------------------------------------------------
    def all(self):
        return list(self._entries)

    # ---------------------------------------------------------
    # Search entries by substring in text
    # ---------------------------------------------------------
    def search(self, query: str):
        q = (query or "").lower()
        return [e for e in self._entries if q in (e.get("text") or "").lower()]

    # ---------------------------------------------------------
    # Clear history
    # ---------------------------------------------------------
    def clear(self):
        debug("[HISTORY] Cleared")
        self._entries.clear()
