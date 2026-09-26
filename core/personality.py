from .utils import debug


class Personality:
    """
    Legacy personality system.
    Modern system uses plugins + response generator,
    but this file remains for compatibility.
    """

    def __init__(self):
        self.style = {
            "prefix": "",
            "suffix": "",
        }

    # ---------------------------------------------------------
    # Set prefix
    # ---------------------------------------------------------
    def set_prefix(self, text: str):
        debug(f"[PERSONALITY] Set prefix: {text}")
        self.style["prefix"] = text

    # ---------------------------------------------------------
    # Set suffix
    # ---------------------------------------------------------
    def set_suffix(self, text: str):
        debug(f"[PERSONALITY] Set suffix: {text}")
        self.style["suffix"] = text

    # ---------------------------------------------------------
    # Apply personality
    # ---------------------------------------------------------
    def apply(self, message: str) -> str:
        prefix = self.style.get("prefix", "")
        suffix = self.style.get("suffix", "")
        return f"{prefix}{message}{suffix}"
