from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSpinBox,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from src.core.exporter import Exporter
from src.core.image_renderer import ImageRenderer
from src.core.srt_parser import SRTParser
from src.models.render_settings import RenderSettings
from src.models.subtitle import Subtitle


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        """Initialize the application window."""

        super().__init__()

        #
        # ----------------------------------------------------
        # Application State
        # ----------------------------------------------------
        #
        self.srt_file: Path | None = None
        self.output_folder: Path | None = None

        self.subtitles: list[Subtitle] = []

        #
        # ----------------------------------------------------
        # Core Services
        # ----------------------------------------------------
        #
        self.parser = SRTParser()
        self.renderer = ImageRenderer()
        self.exporter = Exporter()

        #
        # ----------------------------------------------------
        # Rendering Settings
        # ----------------------------------------------------
        #
        self.render_settings = RenderSettings()

        #
        # ----------------------------------------------------
        # Window Configuration
        # ----------------------------------------------------
        #
        self.setWindowTitle(
            "Subtitle Image Creator Pro"
        )

        self.resize(1200, 820)

        #
        # ----------------------------------------------------
        # Build User Interface
        # ----------------------------------------------------
        #
        self._create_widgets()
        self._create_layout()
        self._create_status_bar()
        self._connect_signals()

        #
        # ----------------------------------------------------
        # Initial Preview
        # ----------------------------------------------------
        #
        self._refresh_preview()
    def _create_widgets(self) -> None:
        """Create all widgets."""

        #
        # Subtitle file
        #
        self.srt_label = QLabel("Subtitle File")

        self.srt_edit = QLineEdit()
        self.srt_edit.setReadOnly(True)
        self.srt_edit.setPlaceholderText(
            "Choose an SRT file..."
        )

        self.srt_button = QPushButton("Browse")

        #
        # Output folder
        #
        self.output_label = QLabel("Output Folder")

        self.output_edit = QLineEdit()
        self.output_edit.setReadOnly(True)
        self.output_edit.setPlaceholderText(
            "Choose an output folder..."
        )

        self.output_button = QPushButton("Browse")

        #
        # Image size
        #
        self.width_label = QLabel("Width")

        self.width_spin = QSpinBox()
        self.width_spin.setRange(320, 8000)
        self.width_spin.setValue(1920)

        self.height_label = QLabel("Height")

        self.height_spin = QSpinBox()
        self.height_spin.setRange(240, 8000)
        self.height_spin.setValue(1080)

        #
        # Preview Image
        #
        self.preview_label = QLabel()

        self.preview_label.setAlignment(
            Qt.AlignCenter
        )

        self.preview_label.setFrameShape(
            QFrame.Box
        )

        self.preview_label.setMinimumSize(
            900,
            500,
        )

        self.preview_label.setText(
            "Preview will appear here"
        )

        self.preview_scroll = QScrollArea()

        self.preview_scroll.setWidget(
            self.preview_label
        )

        self.preview_scroll.setWidgetResizable(
            True
        )

        #
        # Activity Log
        #
        self.activity_log = QTextEdit()

        self.activity_log.setReadOnly(True)

        self.activity_log.append(
            "Application started."
        )

        #
        # Buttons
        #
        self.generate_button = QPushButton(
            "Generate Images"
        )

        self.generate_button.setEnabled(False)

        self.exit_button = QPushButton(
            "Exit"
        )

    def _create_layout(self) -> None:
        """Create the main window layout."""

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(12)

        #
        # ----------------------------------------------------
        # Files
        # ----------------------------------------------------
        #
        files_group = QGroupBox("Files")

        files_layout = QGridLayout(files_group)

        files_layout.addWidget(self.srt_label, 0, 0)
        files_layout.addWidget(self.srt_edit, 0, 1)
        files_layout.addWidget(self.srt_button, 0, 2)

        files_layout.addWidget(self.output_label, 1, 0)
        files_layout.addWidget(self.output_edit, 1, 1)
        files_layout.addWidget(self.output_button, 1, 2)

        #
        # ----------------------------------------------------
        # Image Settings
        # ----------------------------------------------------
        #
        image_group = QGroupBox("Image Settings")

        image_layout = QGridLayout(image_group)

        image_layout.addWidget(self.width_label, 0, 0)
        image_layout.addWidget(self.width_spin, 0, 1)

        image_layout.addWidget(self.height_label, 0, 2)
        image_layout.addWidget(self.height_spin, 0, 3)

        #
        # ----------------------------------------------------
        # Preview
        # ----------------------------------------------------
        #
        preview_group = QGroupBox("Preview")

        preview_layout = QVBoxLayout(preview_group)

        preview_layout.addWidget(self.preview_scroll)

        #
        # ----------------------------------------------------
        # Activity Log
        # ----------------------------------------------------
        #
        log_group = QGroupBox("Activity Log")

        log_layout = QVBoxLayout(log_group)

        log_layout.addWidget(self.activity_log)

        #
        # ----------------------------------------------------
        # Bottom Buttons
        # ----------------------------------------------------
        #
        button_layout = QHBoxLayout()

        button_layout.addWidget(self.generate_button)

        button_layout.addStretch()

        button_layout.addWidget(self.exit_button)

        #
        # ----------------------------------------------------
        # Main Layout
        # ----------------------------------------------------
        #
        main_layout.addWidget(files_group)

        main_layout.addWidget(image_group)

        main_layout.addWidget(
            preview_group,
            stretch=5,
        )

        main_layout.addWidget(
            log_group,
            stretch=2,
        )

        main_layout.addLayout(button_layout)
    def _create_status_bar(self) -> None:
        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def _connect_signals(self) -> None:
        """Connect widget signals."""

        self.exit_button.clicked.connect(self.close)

        self.srt_button.clicked.connect(
            self._browse_srt
        )

        self.output_button.clicked.connect(
            self._browse_output
        )

        self.width_spin.valueChanged.connect(
            self._refresh_preview
        )

        self.height_spin.valueChanged.connect(
            self._refresh_preview
        )

        self.generate_button.clicked.connect(
            self._generate_images
        )

    def _refresh_preview(self) -> None:
        """Render and display the first subtitle."""

        if not self.subtitles:
            self.preview_label.setText(
                "No subtitle loaded."
            )
            return

        self.render_settings.width = self.width_spin.value()
        self.render_settings.height = self.height_spin.value()

        image = self.renderer.render(
            self.subtitles[0],
            self.render_settings,
        )

        #
        # Temporary test
        #
        image.save("preview.png")

        pixmap = QPixmap("preview.png")

        self.preview_label.setPixmap(pixmap)
        self.preview_label.adjustSize()

    def _browse_srt(self) -> None:
        """Select and load an SRT subtitle file."""

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Subtitle File",
            str(Path.home()),
            "Subtitle Files (*.srt)",
        )

        if not filename:
            return

        self.srt_file = Path(filename)

        self.srt_edit.setText(str(self.srt_file))

        try:
            self.subtitles = self.parser.parse(
                self.srt_file
            )

        except Exception as exc:
            self.activity_log.append(
                f"Error loading subtitles: {exc}"
            )

            self.statusBar().showMessage(
                "Failed to load subtitles"
            )

            return

        self.activity_log.append("")

        self.activity_log.append(
            f"Loaded {len(self.subtitles)} subtitles."
        )

        self._refresh_preview()

        self._update_generate_button()

        self.statusBar().showMessage(
            "Subtitle file loaded"
        )

    def _browse_output(self) -> None:
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder",
            str(Path.home()),
        )

        if not folder:
            return

        self.output_folder = Path(folder)

        self.output_edit.setText(
            str(self.output_folder)
        )

        self._update_generate_button()

        self.statusBar().showMessage(
            "Output folder selected"
        )

    def _update_generate_button(self) -> None:
        self.generate_button.setEnabled(
            self.srt_file is not None
            and self.output_folder is not None
        )

    def _generate_images(self) -> None:
        """Generate PNG images for all subtitles."""

        if not self.subtitles:
            return

        if self.output_folder is None:
            return

        self.render_settings.width = self.width_spin.value()
        self.render_settings.height = self.height_spin.value()

        created = self.exporter.export(
            subtitles=self.subtitles,
            settings=self.render_settings,
            output_folder=self.output_folder,
        )

        self.activity_log.append("")

        self.activity_log.append(
            f"{len(created)} images generated."
        )

        self.statusBar().showMessage(
            "Generation completed"
        )