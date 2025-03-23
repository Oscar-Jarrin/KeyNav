from configparser import ConfigParser
import os

class TransparentMode:
    def __init__(self, context, gui):
        #KeyNav, the context class of the state pattern
        self.context = context

        #the good and old gui
        self.gui = gui

        #create the path for the config file with os
        currentDirectory = os.getcwd()
        configFilePath = os.path.join(currentDirectory, "myCode", "configFiles", "config_file.ini")
        self.config = ConfigParser()
        self.config.read(configFilePath)
        self.controlInstructionSection = "control_instructions"

        self.strToFunctionMap = {
            "alternateMode": self.contextToMouseMode,
        }
     
    def handleCombinations(self, currentCombinations):
        for combination in currentCombinations:
            if combination in self.config[self.controlInstructionSection]:
                instructionToExecute = self.config[self.controlInstructionSection][combination]
                if instructionToExecute in self.strToFunctionMap:
                    self.strToFunctionMap[instructionToExecute]()
    
    def contextToMouseMode(self):
        self.context.setToMouseMode()