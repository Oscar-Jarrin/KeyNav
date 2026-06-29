from configparser import ConfigParser
import math
import os
from hardwareSimulators.MouseManager import MouseManager
import sys
from PyQt5.QtWidgets import QApplication

class MouseSimulator:
    def __init__(self, context, gui):
        #KeyNav, the context of the state pattern
        self.context = context

        #the good and old gui
        self.gui = gui

        #the QApp for the gui
        self.app = QApplication(sys.argv)
        #to controll the mouse
        self.mouse = MouseManager()

        #this is my previos way of calling the config file
        ## Get the absolute directory of the current script (e.g., C:\keyNavRoot\SourceCode\StatesAndContext)
        #currentDirectory = os.path.dirname(os.path.abspath(__file__))
        ## Move one level up to reach C:\keyNavRoot\SourceCode
        #sourceCodeDirectory = os.path.dirname(currentDirectory)
        ## Construct the correct path to config_file.ini
        #configFilePath = os.path.join(sourceCodeDirectory, "configFiles", "config_file.ini")
        ##print(f"In mouse state, the route for the config_file is {configFilePath}")
        #self.config = ConfigParser()
        #self.config.read(configFilePath)

        #this is the gpt way of calling the config file
        if getattr(sys, 'frozen', False):  # Running as EXE
            baseDirectory = os.path.dirname(sys.executable)  # Path inside keynav.dist
        else:  # Running as a Python script
            baseDirectory = os.path.dirname(os.path.abspath(__file__))
            baseDirectory = os.path.dirname(baseDirectory)

        exedir = os.path.dirname(sys.executable)
        #print(f"IF I WERE IN .EXE, the route would be {os.path.join(exedir, "configFiles", "config_file.ini")}")
        # Construct the correct path to config_file.ini
        configFilePath = os.path.join(baseDirectory, "configFiles", "config_file.ini")

        #print(f"In MouseState, the route for config_file is {configFilePath}")
        #configFilePath ="C:\keyNavRoot\SourceCode\configFiles\config_file.ini"
        # Read the config file
        self.config = ConfigParser()
        self.config.read(configFilePath) 

        self.mouseInstructionsSection = "mouse_instructions"
        self.controlInstructionSection = "control_instructions"
        

        self.rightClickPressed = False
        self.middleClickPressed = False
        self.leftClickPressed = False
        self.activeZones = set()

        self.MIN_SCROLL_SPEED = 0.2
        self.MAX_SCROLL_SPEED = 10
        self.scrollSpeed = self.MIN_SCROLL_SPEED
        self.scrollAccelerationFactor = 1.02
        self.activeScrollOrientations = set()
        self.lastScrollOrientation = (0,0)
        self.orientationVector = {
            "up":(0, 1),
            "down":(0, -1),
            "left":(-1, 0),
            "right":(1, 0),
        }
        self.MIN_CURSOR_SPEED = 2
        self.MAX_CURSOR_SPEED = 25
        self.cursorSpeed = self.MIN_CURSOR_SPEED
        self.cursorAccelerationFactor = 1.2
        self.activeCursorOrientations = set()
        self.lastCursorOrientation = (0,0)

        self.decelerationFactor = 0.3

        self.strToFunctionMap = {
            "leftClick": self.leftClick,
            "middleClick": self.middleClick,
            "rightClick": self.rightClick,
            "scrollDown": self.scrollDown,
            "scrollUp": self.scrollUp,
            "scrollLeft": self.scrollLeft,
            "scrollRight": self.scrollRight,
            "cursorDown": self.cursorDown,
            "cursorUp": self.cursorUp,
            "cursorLeft": self.cursorLeft,
            "cursorRight": self.cursorRight,
            "mouseToTopLeft": self.cursorToUpLeftSection,
            "mouseToTopMiddle": self.cursorToUpMiddelSection,
            "mouseToTopRight": self.cursorToUpRightSection,
            "cursorToCentralLeftSection": self.cursorToCentralLeftSection,
            "cursorToCentralMiddleSection": self.cursorToCentralMiddleSection,
            "cursorToCentralRightSection": self.cursorToCentralRightSection,  
            "mouseToDownLeft": self.cursorToDownLeftSection,
            "mouseToDownMiddle": self.cursorToDownMiddelSection,
            "mouseToDownRight": self.cursorToDownRightSection,
            "resetCursorPosition": self.resetCursorPosition,
            "swapLeftClick": self.swapLeftClick,
            "swapMiddleClick": self.swapMiddleClick,
            "swapRightClick": self.swapRightClick,
            "resetClicks": self.resetClicks,
            "alternateMode": self.__contextToTransparentMode,
        }


    def handleCombinations(self, currentCombinations):
        if currentCombinations: #if has elements:
            for combination in currentCombinations:
                self.simulateOn(combination)
            self.detectCursorMovement()
            self.detectScroll()
        else:
            self.decelerateCursor()
            self.decelerateScroll()
            self.activeZones.clear()
            self.rightClickPressed = False
            self.middleClickPressed = False
            self.leftClickPressed = False
        #este clear permite que en el siguiente click solo se activen las teclas que siguen siendo presionadas y no se mantengan
        #teclas fantasma
        self.activeCursorOrientations.clear()
        self.activeScrollOrientations.clear()
    
    def simulateOn(self, keySequence: str):
        #print(f"the str of the key sequence recieved by the Mouse Simulator is: {keySequence}")
        instructionToExecute = None
        if keySequence in self.config[self.controlInstructionSection]:
            instructionToExecute = self.config[self.controlInstructionSection][keySequence]
        elif keySequence in self.config[self.mouseInstructionsSection]:
            instructionToExecute = self.config[self.mouseInstructionsSection][keySequence]
        if instructionToExecute != None and instructionToExecute in self.strToFunctionMap:
            self.strToFunctionMap[instructionToExecute]()         
            #print(instructionToExecute)

    #cursor movement
    def cursorUp(self):
        #print("cursor up")
        self.activeCursorOrientations.add("up")
        self.activeCursorOrientations.discard("down")
    def cursorDown(self):
        #print("cursor down")
        self.activeCursorOrientations.add("down")
        self.activeCursorOrientations.discard("up")
    def cursorLeft(self):
        #print("cursor left")
        self.activeCursorOrientations.add("left")
        self.activeCursorOrientations.discard("right")
    def cursorRight(self):
        #print("cursor right")
        self.activeCursorOrientations.add("right")
        self.activeCursorOrientations.discard("left")
    def decelerateCursor(self):
        if self.activeCursorOrientations:
            self.activeCursorOrientations = set()
        if self.cursorSpeed > self.MIN_CURSOR_SPEED:  
            #print(f"I am decelerating at cursor speed {self.cursorSpeed}")
            dx, dy = self.lastCursorOrientation
            dx *= self.cursorAccelerationFactor
            dy *= self.cursorAccelerationFactor
            self.mouse.moveCursor(dx, dy)
            self.cursorSpeed = max(self.cursorSpeed*self.decelerationFactor, self.MIN_CURSOR_SPEED)
    def detectCursorMovement(self):
        if self.activeCursorOrientations:
            #calculate curent orientation vector
            dx = 0
            dy = 0
            for orientation in self.activeCursorOrientations:
                dirx, diry = self.orientationVector[orientation]
                dx += dirx   
                dy += diry
            #normalize diagonal movement
            if dx != 0 and dy != 0:
                length = math.sqrt(dx**2 + dy**2)
                dx /= length
                dy /= length
            #apply acceleration
            dx *= self.cursorSpeed
            dy *= self.cursorSpeed
            #move cursor
            self.mouse.moveCursor(dx, dy)
            #update last orientation vector (including the acceleration)
            self.lastCursorOrientation = (dx, dy)
            #increase speed
            #print(f"I am accelerating at cursor speed {self.cursorSpeed}")
            self.cursorSpeed = min(self.cursorSpeed*self.cursorAccelerationFactor, self.MAX_CURSOR_SPEED)

    #scroll
    def scrollDown(self):
        self.activeScrollOrientations.add("down")
        self.activeCursorOrientations.discard("up")
    def scrollUp(self):
        self.activeScrollOrientations.add("up")
        self.activeCursorOrientations.discard("down")
    def scrollLeft(self):
        self.activeScrollOrientations.add("left")
        self.activeCursorOrientations.discard("right")
    def scrollRight(self):
        self.activeScrollOrientations.add("right")
        self.activeCursorOrientations.discard("left")
    def detectScroll(self):
        if self.activeScrollOrientations:
            #calculate curent orientation vector
            dx = 0
            dy = 0
            for orientation in self.activeScrollOrientations:
                dirx, diry = self.orientationVector[orientation]
                dx += dirx   
                dy += diry
            #normalize diagonal movement
            if dx != 0 and dy != 0:
                length = math.sqrt(dx**2 + dy**2)
                dx /= length
                dy /= length
            #apply acceleration
            dx *= self.scrollSpeed
            dy *= self.scrollSpeed
            #move cursor
            self.mouse.scroll(dx, dy)
            #update last orientation vector (including the acceleration)
            self.lastScrollOrientation = (dx, dy)
            #increase speed
            #print(f"I am scrolling at speed {self.scrollSpeed}")
            self.scrollSpeed = min(self.scrollSpeed*self.scrollAccelerationFactor, self.MAX_SCROLL_SPEED)
    def decelerateScroll(self):
        if self.activeScrollOrientations:
            self.activeScrollOrientations = set()
        if self.scrollSpeed > self.MIN_SCROLL_SPEED:  
            #print(f"I am decelerating at cursor speed {self.scrollSpeed}")
            dx, dy = self.lastScrollOrientation
            dx *= self.scrollAccelerationFactor
            dy *= self.scrollAccelerationFactor
            self.mouse.scroll(dx, dy)
            self.scrollSpeed = max(self.scrollSpeed*self.decelerationFactor, self.MIN_SCROLL_SPEED)
    
    #sections movement 
    def cursorToUpLeftSection(self):
        self.__moveCursotToSection((0,0))
    def cursorToUpMiddelSection(self):
        self.__moveCursotToSection((0,1))
    def cursorToUpRightSection(self):
        self.__moveCursotToSection((0,2))
    def cursorToCentralLeftSection(self):
        self.__moveCursotToSection((1,0))
    def cursorToCentralMiddleSection(self):
        self.__moveCursotToSection((1,1))
    def cursorToCentralRightSection(self):
        self.__moveCursotToSection((1,2))
    def cursorToDownLeftSection(self):
        self.__moveCursotToSection((2,0))
    def cursorToDownMiddelSection(self):
        self.__moveCursotToSection((2,1))
    def cursorToDownRightSection(self):
        self.__moveCursotToSection((2,2))
    def resetCursorPosition(self):
        self.mouse.resetMousePosition()
        #TODO solve a way to draw the grid and still be able to quickly move the cursor
        self._drawZonesIndicatorLines()
    def __moveCursotToSection(self, zoneCoordinates):
        #print(f"the coordinate {zoneCoordinates} is in self.activeZones: {zoneCoordinates in self.activeZones}")
        if zoneCoordinates not in self.activeZones:
            self.activeZones.add(zoneCoordinates)
            coordX, coordY = zoneCoordinates
            self.mouse.moveMouseToSection(coordX,coordY)
        self.cursorSpeed = self.MIN_CURSOR_SPEED

    #clicks
    def leftClick(self):
        if not self.leftClickPressed:
            self.mouse.click("left")
            self.leftClickPressed = True
            self.resetClicks()
    def rightClick(self):
        #print("i pressed right click")
        if not self.rightClickPressed:
            self.mouse.click("right")
            self.rightClickPressed = True
            self.resetClicks()
    def middleClick(self):
        #print("i pressed the middle click")
        if not self.middleClickPressed:
            self.mouse.click("middle")
            self.middleClickPressed = True
            self.resetClicks()
    def resetClicks(self):
        self.mouse.resetAllClicks()

    #swap clicks
    def swapLeftClick(self):
        if not self.leftClickPressed:
            self.mouse.swapStateOfClick("left")
            self.leftClickPressed = True
    def swapMiddleClick(self):
        if not self.middleClickPressed:
            self.mouse.swapStateOfClick("middle")
            self.middleClickPressed = True
    def swapRightClick(self):
        if not self.rightClickPressed:
            self.mouse.swapStateOfClick("right")
            self.rightClickPressed = True
        
    #control instruction
    def __contextToTransparentMode(self):
        self.context.setToTransparentMode()
    
    #gui notification
    def _drawZonesIndicatorLines(self):
        self.gui.drawSeparatorLines()
    