from pathlib import Path

from src.core.image_renderer import ImageRenderer
from src.models.render_settings import RenderSettings
from src.models.subtitle import Subtitle


class Exporter:
    """Exports subtitle images."""

    def __init__(self) -> None:
        self.renderer = ImageRenderer()

    def export(
        self,
        subtitles: list[Subtitle],
        settings: RenderSettings,
        output_folder: Path,
    ) -> list[Path]:
        """
        Render all subtitles and save them as PNG files.

        Returns:
            List of generated image paths.
        """

        output_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        created_files: list[Path] = []

        for subtitle in subtitles:

            image = self.renderer.render(
                subtitle,
                settings,
            )

            filename = (
                output_folder
                / f"{subtitle.index:04d}.png"
            )

            image.save(filename)

            created_files.append(filename)

        return created_files