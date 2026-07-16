from PIL import ImageDraw, ImageFont


class TextLayoutEngine:
    """Lay out subtitle text using pixel measurements."""

    def wrap(
        self,
        text: str,
        draw: ImageDraw.ImageDraw,
        font: ImageFont.FreeTypeFont,
        max_width: int,
    ) -> str:
        """
        Wrap subtitle text so that every line fits inside
        the available pixel width.
        """

        words = text.split()

        if not words:
            return ""

        lines: list[str] = []
        current_line = words[0]

        for word in words[1:]:

            candidate = f"{current_line} {word}"

            left, top, right, bottom = draw.textbbox(
                (0, 0),
                candidate,
                font=font,
            )

            width = right - left

            if width <= max_width:
                current_line = candidate
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)

        return "\n".join(lines)