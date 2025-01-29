import processingLogic.KeyNav as KeyNav
from configparser import ConfigParser
from .State import State
import os

class TransparentMode(State):
    def __init__(self, context: KeyNav):
        print("im in transparentMode")
        self.context = context
        #create the path for the config file with os
        currentDirectory = os.getcwd()
        configFilePath = os.path.join(currentDirectory, "myCode", "configFiles", "transparent_mode_config.ini")
        self.config = ConfigParser()
        self.config.read(configFilePath)
        self.configSectionName = "transparent_mode_config"
        self.strToFunctionMap = {
            "contextToSwapMode": self.contextToSwapMode
        }
     
    #implementing abc method
    def handleInput(self, keySequence):
        if keySequence in self.config[self.configSectionName]:
            instructionToExcecute = self.config[self.configSectionName][keySequence]
            if instructionToExcecute in self.strToFunctionMap:
                self.strToFunctionMap[instructionToExcecute]()