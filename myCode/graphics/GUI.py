import sys
from graphics.DivisorLinesDrawer import DivisorLinesDrawer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QCoreApplication

class GUI:
    def __init__(self):
        self.app = QApplication(sys.argv)
    
    def drawSeparatorLines(self):
        linesDrawer =  DivisorLinesDrawer()
        while linesDrawer.isVisible():
            self.app.processEvents()