# core/engine.py
from typing import Optional

class CentralAIEngine:
    """
    CentralAIEngine: a minimal, self-contained interactive engine.
    Designed to be safe to drop into projects that expect an engine
    with a start() entrypoint. Replace or extend methods as needed.
    """
    def __init__(self, prompt: Optional[str] = "> "):
        self.prompt = prompt or "> "
        self.running = False

    def handle_line(self, line: str) -> None:
        """
        Process a single input line. This default implementation
        echoes the input. Override for real behavior.
        """
        text = (line or "").strip()
        if not text:
            return
        if text.lower() in ("shutdown", "exit", "quit"):
            self.stop()
            return
        # Default behavior: echo back
        print(f"Echo: {text}")

    def start(self) -> None:
        """
        Start the engine REPL loop. Returns when the loop ends.
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
                # input() can return None in some environments; guard against it
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
