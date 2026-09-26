from utils import debug


def generate_response(result):
    """
    Final output stage.
    Converts routed/processed results into printable text.
    """

    debug(f"[RESPONSE] Raw result: {result}")

    if result is None:
        return ""

    # If the result is already a string, return it directly
    if isinstance(result, str):
        return result

    # If the result is a list, join into readable output
    if isinstance(result, list):
        return "\n".join(str(item) for item in result)

    # Fallback: convert to string
    return str(result)
