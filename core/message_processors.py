from .utils import debug


def normalize(text: str) -> str:
    """
    Basic normalization step.
    More processors can be added to the pipeline.
    """
    return text.strip()


def lowercase(text: str) -> str:
    return text.lower()


def processor_pipeline(text: str) -> str:
    """
    Message preprocessing pipeline.
    Each step transforms the incoming user message.
    """
    debug(f"[PROCESSORS] Raw input: {text}")

    steps = [
        normalize,
        # lowercase,   # optional — disabled to preserve user intent
    ]

    for step in steps:
        text = step(text)

    debug(f"[PROCESSORS] Processed: {text}")
    return text
