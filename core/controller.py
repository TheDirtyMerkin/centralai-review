"""
core/controller.py

Controller that owns the engine and exposes a simple run entrypoint.
Keeps controller logic minimal so the engine contains interactive behavior.
"""

from .engine import CentralAIEngine


class CentralAIController:
    """
    High-level controller for the CentralAI application.

    Responsibilities:
    - Instantiate and configure the engine.
    - Provide a simple run() entrypoint for interactive use.
    """

    def __init__(self, prompt: str = "> "):
        self.engine = CentralAIEngine(prompt=prompt)

    def run(self) -> None:
        """Start the engine's interactive loop."""
        self.engine.start()
