from utils import debug


class MemoryManager:
    """
    Simple ephemeral memory store.
    Designed for short-term conversational memory:
    - remember(item): append a memory
    - recall(): return recent memories
    - list(): list all memories
    - clear(): wipe memory
    """

    def __init__(self, max_items: int = 100):
        self._memories = []
        self._max = max_items

    # ---------------------------------------------------------
    # Remember a new item
    # ---------------------------------------------------------
    def remember(self, item: str):
        debug(f"[MEMORY] Remembering: {item}")
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
    def recall(self, count: int = None):
        if count is None:
            return list(self._memories)
        return list(self._memories[-count:])

    # ---------------------------------------------------------
    # List all memories (alias)
    # ---------------------------------------------------------
    def list(self):
        return self.recall()

    # ---------------------------------------------------------
    # Clear memory
    # ---------------------------------------------------------
    def clear(self):
        debug("[MEMORY] Cleared")
        self._memories.clear()
