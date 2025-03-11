from configparser import ConfigParser
import os
from hardwareControllers.MouseManager import MouseManager
from processingLogic.InputManager import InputManager

class MouseSimulator():
    def __init__(self):
        self.listener = InputManager(self)
        self.mouse = MouseManager()
        #create the path for the config file with os
        currentDirectory = os.getcwd()
        configFilePath = os.path.join(currentDirectory, "myCode", "configFiles", "mouse_mode_config.ini")
        self.config = ConfigParser()
        self.config.read(configFilePath)
        self.configSectionName = "mouse_mode_config"
        self.strToFunctionMap = {
            "contextToSwapMode": self.contextToSwapMode,
            "leftClick": self.leftClick,
            "middleClick": self.middleClick,
            "rightClick": self.rightClick,
            "scrollDown": self.scrollDown,
            "scrollUp": self.scrollUp,
            "scrollLeft": self.scrollLeft,
            "scrollRight": self.scrollRight,
            "cursorUp": self.cursorUp,
            "cursorDown": self.cursorDown,
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
            #this is going to be used when I make the effect that the more you press a function, the faster it goes
            "stopAcceleration": self.stopAcceleration, 
            "swapLeftClick": self.swapLeftClick,
            "swapMiddleClick": self.swapMiddleClick,
            "swapRightClick": self.swapRightClick,
        }

    def simulateOn(self, keySequence: str):
        #print(f"the str of the key sequence recieved by the Mouse Simulator is: {keySequence}")
        if keySequence in self.config[self.configSectionName]:
            instructionToExcecute = self.config[self.configSectionName][keySequence]
            if instructionToExcecute in self.strToFunctionMap:
                self.strToFunctionMap[instructionToExcecute]()         
                #print(self.strToFunctionMap[instructionToExcecute])
                #print(self.config.sections())
                #print(instructionToExcecute)

    def cursorToUpLeftSection(self):
        self.mouse.moveMouseToSection(0,0)
    
    def cursorToUpMiddelSection(self):
        self.mouse.moveMouseToSection(0,1)

    def cursorToUpRightSection(self):
        self.mouse.moveMouseToSection(0,2)

    def cursorToCentralLeftSection(self):
        self.mouse.moveMouseToSection(1,0)

    def cursorToCentralMiddleSection(self):
        self.mouse.moveMouseToSection(1,1)

    def cursorToCentralRightSection(self):
        self.mouse.moveMouseToSection(1,2)

    def cursorToDownLeftSection(self):
        self.mouse.moveMouseToSection(2,0)
    
    def cursorToDownMiddelSection(self):
        self.mouse.moveMouseToSection(2,1)

    def cursorToDownRightSection(self):
        self.mouse.moveMouseToSection(2,2)

    def resetCursorPosition(self):
        self.mouse.resetMousePosition()
    
    def leftClick(self):
        self.mouse.click("left")

    def rightClick(self):
        self.mouse.click("right")

    def middleClick(self):
        self.mouse.click("middle")

    def scrollDown(self):
        self.mouse.scroll("down")

    def scrollUp(self):
        self.mouse.scroll("up")

    def scrollLeft(self):
        self.mouse.scroll("left")

    def scrollRight(self):
        self.mouse.scroll("right")

    def cursorUp(self):
        self.mouse.moveCursor("up")
        
    def cursorDown(self):
        self.mouse.moveCursor("down")

    def cursorLeft(self):
        self.mouse.moveCursor("left")

    def cursorRight(self):
        self.mouse.moveCursor("right")
    
    def stopAcceleration(self):
        self.mouse.stopAcceleration()
    
    def swapLeftClick(self):
        self.mouse.swapStateOfClick("left")

    def swapMiddleClick(self):
        self.mouse.swapStateOfClick("middle")
    
    def swapRightClick(self):
        self.mouse.swapStateOfClick("right")
        
    def contextToSwapMode(self):
        pass
