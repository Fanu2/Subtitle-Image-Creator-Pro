from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class RenderSettings:
    """Configuration used to render subtitle images."""

    #
    # Image
    #
    width: int = 1920
    height: int = 1080

    #
    # Background
    #
    background_color: str = "black"

    #
    # Text
    #
    text_color: str = "white"
    font_path: Path | None = None
    font_size: int = 96

    #
    # Text outline
    #
    stroke_color: str = "black"
    stroke_width: int = 3

    #
    # Layout
    #
    margin: int = 80
    line_spacing: int = 12

    #
    # Alignment
    #
    horizontal_alignment: str = "center"
    vertical_alignment: str = "bottom"

    #
    # Preview
    #
    preview_scale: float = 1.0