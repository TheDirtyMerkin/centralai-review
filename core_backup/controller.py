# core/controller.py
from .engine import CentralAIEngine

class CentralAIController:
    """
    Controller that owns the engine and exposes a simple run entrypoint.
    Keeps logic minimal so engine contains interactive behavior.
    """
    def __init__(self, prompt: str = "> "):
        self.engine = CentralAIEngine(prompt=prompt)

    def run(self):
        """Start the engine's interactive loop."""
        self.engine.start()
