import mouse
from pynput.mouse import Controller
from hardwareSimulators.ScreenZonesMaganer import  ScreenZonesManager

class MouseManager:
    def __init__(self):
        self.sectionsManager = ScreenZonesManager()
        self.mouse = Controller()

    def scroll(self, dx, dy):
        self.mouse.scroll(dx, dy)

    def moveMouseToSection(self, coodtinateX, coordinateY):
       self.mouse.position = self.sectionsManager.selectSubZone(coodtinateX, coordinateY)

    def resetMousePosition(self):
        self.mouse.position = self.sectionsManager.resetZoneToScreen()
    
    def resetMouseClicks(self):
        mouse.release("left")
        mouse.release("middle")
        mouse.release("right")

    def swapStateOfClick(self, button: str):
        if mouse.is_pressed(button):
            mouse.release(button)
        else:
            mouse.press(button)

    def click(self, button: str):
        mouse.click(button)

    def moveCursor(self, dx, dy):
        #when Pynput.mouse.Controller() recieves (0, -1), it moves up, and with (0, 1) down
        #the adaptVector swaps it so that it adapts to normal bidimensional cartesian coordinates
        dx, dy = self.__vectorToPynputFormat(dx, dy)
        self.mouse.move(dx, dy)

    def __vectorToPynputFormat(self, dx, dy):
        return dx, dy*(-1)
            
    def resetAllClicks(self):
        if mouse.is_pressed("left"):
            mouse.release("left")
        if mouse.is_pressed("right"):
            mouse.release("right")
        if mouse.is_pressed("middle"):
            mouse.release("middle")