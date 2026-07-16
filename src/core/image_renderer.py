from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from src.core.text_layout import TextLayoutEngine
from src.models.render_settings import RenderSettings
from src.models.subtitle import Subtitle


class ImageRenderer:
    """Render subtitle text into an image."""

    BACKGROUND_COLOURS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "blue": (25, 45, 120),
        "green": (20, 80, 20),
        "red": (120, 20, 20),
        "gray": (70, 70, 70),
        "purple": (70, 40, 100),
    }

    TEXT_COLOURS = {
        "white": (255, 255, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "green": (0, 255, 0),
        "red": (255, 80, 80),
        "orange": (255, 170, 0),
    }

    def __init__(self) -> None:
        self.layout = TextLayoutEngine()

    def render(
        self,
        subtitle: Subtitle,
        settings: RenderSettings,
    ) -> Image.Image:
        """Render a subtitle into a Pillow image."""

        image = Image.new(
            "RGB",
            (settings.width, settings.height),
            self._background_colour(settings),
        )

        draw = ImageDraw.Draw(image)

        font = self._load_font(settings)

        text = self.layout.wrap(
            text=subtitle.text,
            draw=draw,
            font=font,
            max_width=settings.width - (2 * settings.margin),
        )

        left, top, right, bottom = draw.multiline_textbbox(
            (0, 0),
            text,
            font=font,
            align=settings.horizontal_alignment,
            spacing=settings.line_spacing,
        )

        text_width = right - left
        text_height = bottom - top

        x, y = self._calculate_position(
            text_width,
            text_height,
            settings,
        )

        draw.multiline_text(
            (x, y),
            text,
            font=font,
            fill=self._text_colour(settings),
            align=settings.horizontal_alignment,
            spacing=settings.line_spacing,
            stroke_width=settings.stroke_width,
            stroke_fill=settings.stroke_color,
        )

        return image

    def _calculate_position(
        self,
        text_width: int,
        text_height: int,
        settings: RenderSettings,
    ) -> tuple[int, int]:
        """Calculate subtitle position."""

        if settings.horizontal_alignment == "left":
            x = settings.margin

        elif settings.horizontal_alignment == "right":
            x = (
                settings.width
                - text_width
                - settings.margin
            )

        else:
            x = (
                settings.width
                - text_width
            ) // 2

        if settings.vertical_alignment == "top":
            y = settings.margin

        elif settings.vertical_alignment == "center":
            y = (
                settings.height
                - text_height
            ) // 2

        else:
            y = (
                settings.height
                - text_height
                - settings.margin
            )

        return x, y

    def _background_colour(
        self,
        settings: RenderSettings,
    ) -> tuple[int, int, int]:
        """Return background colour."""

        return self.BACKGROUND_COLOURS.get(
            settings.background_color.lower(),
            (0, 0, 0),
        )

    def _text_colour(
        self,
        settings: RenderSettings,
    ) -> tuple[int, int, int]:
        """Return text colour."""

        return self.TEXT_COLOURS.get(
            settings.text_color.lower(),
            (255, 255, 255),
        )

    def _load_font(
        self,
        settings: RenderSettings,
    ) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        """Load the selected font."""

        if settings.font_path is not None:
            return ImageFont.truetype(
                str(settings.font_path),
                settings.font_size,
            )

        candidates = (
            Path("C:/Windows/Fonts/arial.ttf"),
            Path("C:/Windows/Fonts/calibri.ttf"),
            Path("C:/Windows/Fonts/verdana.ttf"),
            Path("C:/Windows/Fonts/tahoma.ttf"),
        )

        for font_path in candidates:
            if font_path.exists():
                return ImageFont.truetype(
                    str(font_path),
                    settings.font_size,
                )

        return ImageFont.load_default()