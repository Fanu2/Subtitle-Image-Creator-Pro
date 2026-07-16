from pathlib import Path

from src.core.srt_parser import SRTParser

parser = SRTParser()

subtitles = parser.parse(Path("test.srt"))

for subtitle in subtitles:
    print(subtitle)