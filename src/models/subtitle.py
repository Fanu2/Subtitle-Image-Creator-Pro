from dataclasses import dataclass


@dataclass(slots=True)
class Subtitle:
    """Represents one subtitle."""

    index: int
    start: str
    end: str
    text: str