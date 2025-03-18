from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import sys

class TransparentOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Enable transparency
        self.showFullScreen()  # Cover the full screen

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Set semi-transparent pen for lines
        pen = QPen(QColor(168, 255, 217, 100))  # White with 150 alpha (semi-transparent)
        pen.setWidth(8)  # Line thickness
        painter.setPen(pen)

        # Get screen dimensions
        width = self.width()
        height = self.height()

        # Draw vertical lines (divide width into 3 equal parts)
        painter.drawLine(width // 3, 0, width // 3, height)
        painter.drawLine(2 * width // 3, 0, 2 * width // 3, height)

        # Draw horizontal lines (divide height into 3 equal parts)
        painter.drawLine(0, height // 3, width, height // 3)
        painter.drawLine(0, 2 * height // 3, width, 2 * height // 3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentOverlay()
    window.show()
    sys.exit(app.exec_())
