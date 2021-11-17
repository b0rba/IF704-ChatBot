from typing import Text


def is_empty_or_none(text: Text) -> bool:
    return text is None or text == ""
