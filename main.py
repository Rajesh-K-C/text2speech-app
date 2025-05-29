import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QTextEdit,
    QLabel,
    QSizePolicy,
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.voice_combo = None
        self.text_edit = None
        self.play_button = None
        self.setWindowTitle("Text To Speech App")
        self.setFixedSize(600, 300)
        self.init_ui()

    def init_ui(self):
        # Voice selection
        voice_label = QLabel("Voice:")
        self.voice_combo = QComboBox()
        self.voice_combo.addItems(["Voice 1", "Voice 2", "Voice 3"])

        voice_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.voice_combo.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Voice section layout
        voice_layout = QHBoxLayout()
        voice_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        voice_layout.addWidget(voice_label)
        voice_layout.addWidget(self.voice_combo)

        # Text input
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter your text")
        self.style()

        # Play button
        self.play_button = QPushButton("Play")
        self.play_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Layout
        layout = QVBoxLayout()
        layout.addLayout(voice_layout)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.play_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
