import processingLogic.KeyNav as KeyNav
from configparser import ConfigParser
from .State import State
import os

class SwapMode(State):
    def __init__(self, context: KeyNav):
        print("im in swapMode")
        self.context = context
        #create the path for the config file with os
        currentDirectory = os.getcwd()
        configFilePath = os.path.join(currentDirectory, "myCode", "configFiles", "mouse_mode_config.ini")
        self.config = ConfigParser()
        self.config.read(configFilePath)
        self.configSectionName = "swap_mode_config"
        self.strToFunctionMap = {
            "contextToWriteMode": self.contextToWriteMode,
            "contextToMouseMode": self.contextToMouseMode,
            "contextToTransparentMode": self.contextToTransparentMode,
            "contextToPreviousMode": self.contextToPreviousMode
        }

    def handleInput(self, keySequence: str):
        print(f"the keysequence that the handle input from the swapMode is: {keySequence}")
        print(self.config[self.configSectionName])
        if keySequence in self.config[self.configSectionName]:
            print("I entered the first if")
            instructionToExcecute = self.config[self.configSectionName][keySequence]
            if instructionToExcecute in self.strToFunctionMap:
                print("I entered the secod if")
                self.strToFunctionMap[instructionToExcecute]()         
                print(f"the {instructionToExcecute} has been excecuted")
            print("the keysequence was found in the config file")

    def contextToWriteMode(self):
        self.context.setToWriteMode()

    def contextToMouseMode(self):
        self.context.setToMouseMode()
   
    def contextToPreviousMode(self):
        self.context.setToPreviousMode() 

    def contextToTransparentMode(self):
        self.context.setToTransparentMode()
