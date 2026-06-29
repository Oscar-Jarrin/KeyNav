from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QTimer
from PIL import Image
import numpy as np

class DivisorLinesDrawer(QWidget):
    def __init__(self):
        super().__init__()

        # Set Full-Screen Transparent Overlay
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # Get screen size dynamically
        screen = QApplication.primaryScreen().size()
        self.screen_width = screen.width()
        self.screen_height = screen.height()

        # Determine screen brightness and choose color
        self.isDarkMode = self.detectScreenBrightness()
        
        # Generate grid lines
        self.mainGridLines = self.generateMainGridLines()
        self.secondaryGridLines = self.generateSecondaryGridLines()

        # Shrinking parameters
        self.mainLineWidth = 30
        self.secondaryLineWidth = 15
        self.secondaryLinesShrinkRate = 1
        self.mainLinesShrinkRate = 2  # Shrinking speed
        self.minLineWidth = 0  # Stop shrinking at this width
        
        # QTimer to repaint the lines and simulate the shrinking 
        self.timer = QTimer()
        self.timer.timeout.connect(self.shrinkLines)
        self.timer.start(15)

        # First events for showing the screen
        self.show()
        #self.update()
        #QApplication.processEvents()
        #print("I finihed building the Drawer")

    def shrinkLines(self):
        #print("I am in shrinkLines")
        if self.mainLineWidth > self.minLineWidth or self.secondaryLineWidth > self.minLineWidth:
            self.mainLineWidth = max(self.mainLineWidth - self.mainLinesShrinkRate, self.minLineWidth)
            self.secondaryLineWidth = max(self.secondaryLineWidth - self.secondaryLinesShrinkRate, self.minLineWidth)
            self.update()
        else:
            self.timer.stop()
            self.close()
            self.windowClosed()

    def windowClosed(self):
        """Ensures the event loop thread stops when the drawer closes."""
        if hasattr(self, "eventLoopThread") and self.eventLoopThread.isRunning():
            self.eventLoopThread.quit()
            self.eventLoopThread.wait()  # Wait for the thread to exit

    def paintEvent(self, event):
            """ Draws the grid lines dynamically. """
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            # Choose contrasting colors based on screen brightness
            if self.isDarkMode:
                mainColor = QColor(50, 50, 50, 180)  # Dark mode → Darker grid
                secondaryColor = QColor(80, 80, 80, 150)
            else:
                mainColor = QColor(220, 220, 220, 180)  # Light mode → Lighter grid
                secondaryColor = QColor(180, 180, 180, 150)
            
            if self.mainLineWidth > 0:
                pen = QPen(mainColor)
                pen.setWidth(self.mainLineWidth)
                painter.setPen(pen)
                for line in self.mainGridLines:
                    painter.drawLine(*line)

            if self.secondaryLineWidth > 0:
                pen.setColor(secondaryColor)
                pen.setWidth(self.secondaryLineWidth)
                painter.setPen(pen)
                for line in self.secondaryGridLines:
                    painter.drawLine(*line)

    def generateMainGridLines(self):
        """Generates the 6 main lines that divide the screen into a 3x3 grid."""
        third_w = self.screen_width // 3
        third_h = self.screen_height // 3
        main_lines = []

        # Vertical lines
        for i in range(1, 3):
            x = i * third_w
            main_lines.append((x, 0, x, self.screen_height))

        # Horizontal lines
        for i in range(1, 3):
            y = i * third_h
            main_lines.append((0, y, self.screen_width, y))

        return main_lines

    def generateSecondaryGridLines(self):
        """Generates the remaining 10 lines that divide the screen into a 9x9 grid."""
        ninth_w = self.screen_width // 9
        ninth_h = self.screen_height // 9
        sub_lines = []

        # Vertical lines (excluding the 3x3 grid lines)
        for i in range(1, 9):
            if i % 3 != 0:  # Skip lines that overlap with 3x3 grid
                x = i * ninth_w
                sub_lines.append((x, 0, x, self.screen_height))

        # Horizontal lines (excluding the 3x3 grid lines)
        for i in range(1, 9):
            if i % 3 != 0:  # Skip lines that overlap with 3x3 grid
                y = i * ninth_h
                sub_lines.append((0, y, self.screen_width, y))

        return sub_lines

    def detectScreenBrightness(self):
        """Captures a screenshot and determines the average brightness."""
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0).toImage()

        # Convert QImage to numpy array
        buffer = screenshot.bits().asstring(screenshot.width() * screenshot.height() * 4)  # RGBA (4 bytes per pixel)
        img = Image.frombytes("RGBA", (screenshot.width(), screenshot.height()), buffer)
        
        # Convert to grayscale and compute brightness
        grayscale_img = img.convert("L")  # Convert to grayscale
        brightness = np.array(grayscale_img).mean()  # Compute average brightness
        
        #print(f"Screen brightness: {brightness}")  # Debugging
        
        return brightness > 128  # If brightness is high, use dark lines