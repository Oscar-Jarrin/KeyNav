import keyboard.mouse
from pynput.mouse import Controller, Button
from hardwareControllers.ScreenZonesMaganer import  ScreenZonesManager
import keyboard

class MouseManager:
    def __init__(self):
        self.sectionsManager = ScreenZonesManager()
        self.mouse = Controller()

        self.initialSpeed = 0.8
        self.speed = self.initialSpeed
        self.MAX_SPEED = 25 

    def moveMouseToSection(self, coodtinateX, coordinateY):
       self.mouse.position = self.sectionsManager.selectSubZone(coodtinateX, coordinateY)

    def resetMousePosition(self):
        self.mouse.position = self.sectionsManager.resetZoneToScreen()
    
    def swapStateOfClick(self, button: str):
        if keyboard.mouse.is_pressed(button):
            keyboard.mouse.release(button)
        else:
            keyboard.mouse.press(button)

    def click(self, button: str):
        keyboard.mouse.click(button)

    def scroll(self, orientation: str):
        self.__increaseSpeed()
        dx = 0 
        dy = 0
        if orientation == "down":
            dy = -0.5 - self.speed
        elif orientation == "up":
            dy = 0.5 + self.speed
        elif orientation == "left":
            dx = -0.5 - self.speed
        elif orientation == "right": 
            dx = 0.5 + self.speed
        self.mouse.scroll(dx, dy)

    def moveCursor(self, orientation: str):
        self.__increaseSpeed()
        dx = 0 
        dy = 0
        if orientation == "down":
            dy = -0.5 - self.speed
        elif orientation == "up":
            dy = 0.5 + self.speed
        elif orientation == "left":
            dx = -0.5 - self.speed
        elif orientation == "right": 
            dx = 0.5 + self.speed
        self.mouse.move(dx, dy)

    def __increaseSpeed(self):
        if self.speed < self.MAX_SPEED:
            self.speed = self.speed*1.15 

    def stopAcceleration(self):
        self.speed = self.initialSpeed

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        