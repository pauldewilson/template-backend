"""
General utility functions.
"""

from app.logging import logger


def string_snippet(snippet: str) -> str:
    """
    Takes in a string and shows
    the first 2 chars then ...
    then the last 2 chars.

    Only truncates if the string
    is >= 10 chars.
    """
    if not isinstance(snippet, str):
        logger.warning("string_snippet: snippet is not a string. %s", snippet)
        return snippet
    if len(snippet) >= 7:
        return f"{snippet[:2]}...{snippet[-2:]}"
    return snippet
