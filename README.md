# Subtitle Image Creator Pro

A modern Python desktop application for converting **SRT subtitle files** into high-quality PNG subtitle images.

Built with **Python**, **PySide6**, and **Pillow**.

---

# Features

## Current Version (v0.1)

✔ Modern desktop GUI

✔ Load SRT subtitle files

✔ Parse subtitle timing and text

✔ Automatic word wrapping

✔ High-quality subtitle rendering

✔ TrueType font support

✔ Adjustable image resolution

✔ Batch generation of PNG images

✔ Configurable text colours

✔ Configurable background colours

✔ Text outline (stroke)

✔ Export one PNG image per subtitle

---

# Example Workflow

```
Movie.srt
        │
        ▼
Subtitle Image Creator Pro
        │
        ▼
0001.png
0002.png
0003.png
...
0035.png
```

---

# Screenshot

(Add screenshots here)

```
docs/images/main_window.png
```

---

# Project Structure

```
SubtitleImageCreatorPro/

│
├── main.py
│
├── src/
│   │
│   ├── core/
│   │      exporter.py
│   │      image_renderer.py
│   │      srt_parser.py
│   │      text_layout.py
│   │
│   ├── models/
│   │      render_settings.py
│   │      subtitle.py
│   │
│   └── ui/
│          main_window.py
│
├── requirements.txt
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Fanu2/Subtitle-Image-Creator-Pro.git
```

Enter the project folder.

```bash
cd Subtitle-Image-Creator-Pro
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Running

```bash
python main.py
```

---

# How to Use

## Step 1

Browse and select an SRT subtitle file.

Example

```
movie.srt
```

---

## Step 2

Select an output folder.

Example

```
D:\SubtitleImages
```

---

## Step 3

Choose image size.

Example

```
1920 × 1080
```

---

## Step 4

Click

```
Generate Images
```

---

## Result

```
0001.png

0002.png

0003.png

...

0035.png
```

One image is generated for every subtitle.

---

# Rendering Engine

The rendering engine supports

- Automatic subtitle wrapping

- Multiple subtitle lines

- Center alignment

- Outline (stroke)

- Custom font size

- Background colours

- Text colours

- Adjustable margins

---

# Technologies Used

- Python 3.14+

- PySide6

- Pillow (PIL)

- pysrt

---

# Current Architecture

```
SRT File

      │

      ▼

 SRT Parser

      │

      ▼

 Subtitle Objects

      │

      ▼

 Text Layout Engine

      │

      ▼

 Image Renderer

      │

      ▼

 PNG Exporter

      │

      ▼

 PNG Images
```

---

# Roadmap

## Version 0.2

- Better live preview

- Progress bar

- Image counter

- Better typography

---

## Version 0.3

- Font selection

- Colour picker

- Background picker

- Font browser

---

## Version 0.4

- Drag & Drop

- Recent files

- Settings persistence

---

## Version 0.5

- Transparent PNG

- JPG export

- Multiple export profiles

---

## Version 1.0

- Complete professional subtitle image creator

- Batch processing

- High-quality rendering

- Theme support

- Export presets

- Production ready

---

# Contributing

Contributions, bug reports, feature requests and pull requests are welcome.

---

# License

MIT License

---

# Author

**Jasvir Singh Sidhu**

GitHub

https://github.com/Fanu2

---

# Acknowledgements

- Python

- PySide6

- Pillow

- pysrt

---

# Version

Current Release

```
v0.1.0
```