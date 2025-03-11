from configparser import ConfigParser
import os

class TransparentMode():
    def __init__(self):
        #print("im in transparentMode")
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