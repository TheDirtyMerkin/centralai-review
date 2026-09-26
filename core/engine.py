"""
core/engine.py

A minimal, self-contained interactive engine with a safe REPL entrypoint.
This implementation is intentionally simple so it can be dropped into projects
and extended or replaced as needed.
"""

from typing import Optional


class CentralAIEngine:
    """
    CentralAIEngine: minimal interactive engine.

    Public methods:
    - start(): run the REPL loop until stopped
    - stop(): request the loop to stop
    - handle_line(line): process a single input line (override for real behavior)
    """

    def __init__(self, prompt: Optional[str] = None):
        self.prompt = prompt or "> "
        self.running = False

    def handle_line(self, line: str) -> None:
        """
        Process a single input line.

        Default behavior: echo the input. Override this method to implement
        real command handling or integration with the rest of the system.
        """
        text = (line or "").strip()
        if not text:
            return

        lowered = text.lower()
        if lowered in ("shutdown", "exit", "quit"):
            self.stop()
            return

        # Default behavior: echo back
        print(f"Echo: {text}")

    def start(self) -> None:
        """
        Start the engine REPL loop. Returns when the loop ends.
        Safe to call multiple times; subsequent calls while running are no-ops.
        """
        if self.running:
            return

        self.running = True
        print("CentralAI Engine started. Type messages. Type 'shutdown' to exit.")
        try:
            while self.running:
                try:
                    line = input(self.prompt)
                except (EOFError, KeyboardInterrupt):
                    print("\nShutting down (input closed).")
                    break

                # Guard against environments where input() may return None
                if line is None:
                    continue

                self.handle_line(line)
        finally:
            self.running = False

    def stop(self) -> None:
        """Stop the running loop cleanly."""
        if self.running:
            print("Shutting down.")
        self.running = False


def main() -> None:
    engine = CentralAIEngine()
    engine.start()


if __name__ == "__main__":
    main()
