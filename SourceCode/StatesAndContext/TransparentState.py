from configparser import ConfigParser
import sys
import os
class TransparentMode:
    def __init__(self, context, gui):
        #KeyNav, the context class of the state pattern
        self.context = context

        #the good and old gui
        self.gui = gui

        #this is my previos way of calling the config file
        ## Get the absolute directory of the current script (e.g., C:\keyNavRoot\SourceCode\StatesAndContext)
        #currentDirectory = os.path.dirname(os.path.abspath(__file__))
        ## Move one level up to reach C:\keyNavRoot\SourceCode
        #sourceCodeDirectory = os.path.dirname(currentDirectory)
        ## Construct the correct path to config_file.ini
        #configFilePath = os.path.join(sourceCodeDirectory, "configFiles", "config_file.ini")
        #print(f"In mouse state, the route for the config_file is {configFilePath}")
        #self.config = ConfigParser()
        #self.config.read(configFilePath)

        #this is the gpt way of calling the config file
        # Determine base directory, whether running as script or exe
        if getattr(sys, 'frozen', False):
            # Running as an executable (PyInstaller or Nuitka)
            baseDirectory = os.path.dirname(os.path.abspath(sys.executable))
        else:
            # Running as a normal Python script
            baseDirectory = os.path.dirname(os.path.abspath(__file__))

        # Move one level up to reach "SourceCode"
        sourceCodeDirectory = os.path.dirname(baseDirectory)

        # Construct the correct path to config_file.ini
        configFilePath = os.path.abspath(os.path.join(sourceCodeDirectory, "configFiles", "config_file.ini"))

        print(f"In MouseState, the route for config_file is {configFilePath}")

        # Read the config file
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