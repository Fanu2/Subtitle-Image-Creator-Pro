from textwrap import wrap


class TextWrapper:
    """Wrap subtitle text into multiple lines."""

    def wrap(
        self,
        text: str,
        max_characters: int = 38,
    ) -> str:
        """
        Wrap text into multiple lines.

        Returns:
            Wrapped subtitle text.
        """

        lines = wrap(
            text,
            width=max_characters,
            break_long_words=False,
            break_on_hyphens=False,
        )

        return "\n".join(lines)