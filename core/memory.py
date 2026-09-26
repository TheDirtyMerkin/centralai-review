"""
core/memory.py

Simple ephemeral memory store for short-term conversational memory.

Public methods:
- remember(item: str) -> Optional[str]
- recall(count: Optional[int] = None) -> list[str]
- list() -> list[str]  (alias for list_all)
- list_all() -> list[str]
- clear() -> None
"""

from typing import List, Optional


class MemoryManager:
    """
    Simple ephemeral memory store.

    Keeps the most recent items up to a configurable capacity.
    """

    def __init__(self, max_items: int = 100) -> None:
        self._memories: List[str] = []
        self._max: int = max_items

    # ---------------------------------------------------------
    # Remember a new item
    # ---------------------------------------------------------
    def remember(self, item: str) -> Optional[str]:
        """
        Append a memory item and return it.
        Returns None if the provided item is empty or falsy.
        """
        try:
            from .utils import debug  # type: ignore
            debug(f"[MEMORY] Remembering: {item}")
        except Exception:
            pass

        if not item:
            return None

        # Keep most recent items up to capacity
        self._memories.append(item)
        if len(self._memories) > self._max:
            self._memories = self._memories[-self._max :]

        return item

    # ---------------------------------------------------------
    # Recall recent memories
    # ---------------------------------------------------------
    def recall(self, count: Optional[int] = None) -> List[str]:
        """
        Return recent memories.
        If count is None, return all memories; otherwise return the last `count` items.
        """
        if count is None:
            return list(self._memories)
        if count <= 0:
            return []
        return list(self._memories[-count:])

    # ---------------------------------------------------------
    # List all memories (alias)
    # ---------------------------------------------------------
    def list_all(self) -> List[str]:
        """Return all memories (alias-friendly name to avoid shadowing built-in)."""
        return self.recall()

    # Keep a backward-compatible alias named `list` for existing callers.
    list = list_all  # type: ignore

    # ---------------------------------------------------------
    # Clear memory
    # ---------------------------------------------------------
    def clear(self) -> None:
        """Clear all stored memories."""
        try:
            from .utils import debug  # type: ignore
            debug("[MEMORY] Cleared")
        except Exception:
            pass
        self._memories.clear()
