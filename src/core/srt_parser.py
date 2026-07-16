from pathlib import Path

import pysrt

from src.models.subtitle import Subtitle


class SRTParser:
    """Parses SRT subtitle files."""

    def parse(
        self,
        filename: Path,
    ) -> list[Subtitle]:
        """
        Parse an SRT file.

        Returns:
            List of Subtitle objects.
        """

        subtitles: list[Subtitle] = []

        subs = pysrt.open(
            str(filename),
            encoding="utf-8",
        )

        for item in subs:

            subtitles.append(
                Subtitle(
                    index=item.index,
                    start=str(item.start),
                    end=str(item.end),
                    text=item.text.replace("\n", " "),
                )
            )

        return subtitles