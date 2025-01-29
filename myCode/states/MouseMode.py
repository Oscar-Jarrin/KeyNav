import processingLogic.KeyNav as KeyNav
from configparser import ConfigParser
from .State import State
import os
class MouseMode(State):
    def __init__(self, context: KeyNav):
        self.context = context
        print("im in mouseMode")
        #create the path for the config file with os
        currentDirectory = os.getcwd()
        configFilePath = os.path.join(currentDirectory, "myCode", "configFiles", "mouse_mode_config.ini")
        self.config = ConfigParser()
        self.config.read(configFilePath)
        self.configSectionName = "mouse_mode_config"
        #print(currentDirectory)
        #print(self.config)
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
            "cursorRight": self.cursorRight
        }

    def leftClick(self):
        print("the hw is pressing left click")

    def rightClick(self):
        print("the hw is pressing right click") 

    def middleClick(self):
        print("the hw is pressing middle click")

    def scrollDown(self):
        print("the hw is scrolling down") 
    
    def scrollUp(self):
        print("the hw is scrolling up")

    def scrollRight(self):
        print("the hw is scrolling right")

    def scrollLeft(self):
        print("the hw is scolling left")

    def cursorUp(self):
        print("the hw is moving the cursor up")

    def cursorDown(self):
        print("the hw is moving the cursor down")

    def cursorRight(self):
        print("the hw is moving the cursor right")

    def cursorLeft(self):
        print("the hw is moving the cursor left")

    #implementing abc method
    def handleInput(self, keySequence: str):
        if keySequence in self.config[self.configSectionName]:
            instructionToExcecute = self.config[self.configSectionName][keySequence]
            if instructionToExcecute in self.strToFunctionMap:
                self.strToFunctionMap[instructionToExcecute]()         
                #print(self.strToFunctionMap[instructionToExcecute])
                #print(self.config.sections())
                #print(instructionToExcecute)