from pathlib import Path

from src.core.image_renderer import ImageRenderer
from src.models.render_settings import RenderSettings
from src.models.subtitle import Subtitle

subtitle = Subtitle(
    index=1,
    start="00:00:00,000",
    end="00:00:04,000",
    text="Hello from Subtitle Image Creator!",
)

settings = RenderSettings()

renderer = ImageRenderer()

image = renderer.render(
    subtitle,
    settings,
)

image.save(Path("preview.png"))

print("preview.png created.")