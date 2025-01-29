import processingLogic.KeyNav as KeyNav
from configparser import ConfigParser, ExtendedInterpolation
from .State import State
from .PrintableSequenceConversor import PrintableSequenceConversor
import os
import sys

class WriteMode(State):
    def __init__(self, context: KeyNav):
        self.context = context
        print("im in write mode")
        #create the path for the config file with os
        currentDirectory = os.getcwd()
        configFilePath = os.path.join(currentDirectory, "myCode", "configFiles", "write_mode_config.ini")
        self.config = ConfigParser()
        self.config.read(configFilePath)
        self.configSectionName = "write_mode_config"
        self.printableFormatConversor = PrintableSequenceConversor()
        self.strToFunctionMap = {
            "contextToSwapMode": self.contextToSwapMode,
            "deleteChar": self.deleteChar,
            "deleteWord": self.deleteWord,
            "writeCursorUp": self.writeCursorUp,
            "writeCursorDown": self.writeCursorDown,
            "writeCursorLeft": self.writeCursorLeft,
            "writeCursorRight": self.writeCursorRigh
        }

    #implementing abc method
    def handleInput(self, keySequence: str):
        #this is going to be used when I add shortcuts to writeMode but for now,
        #the config file is empty
        print(f"the input from the handle input in writeMode is: {keySequence}")
        if keySequence in self.config[self.configSectionName]:
            instructionToExcecute = self.config[self.configSectionName][keySequence]
            if instructionToExcecute in self.strToFunctionMap:
                self.strToFunctionMap[instructionToExcecute]()         
                print(f"the {instructionToExcecute} has been excecuted")
        else: 
            textWithoutGhostKeys = self.printableFormatConversor.transformToPrintableSequence(keySequence)
            if textWithoutGhostKeys != "":
                sys.stdout.write(textWithoutGhostKeys)
                sys.stdout.flush()
    
    def deleteChar(self):
        print("the hw is deleting a char")
    
    def deleteWord(self):
        print("the hw is deleting a word")

    def writeCursorUp(self):
        print("the hw is pressing the up key")
    
    def writeCursorDown(self):
        print("the hw is pressing the down key")

    def writeCursorLeft(self):
        print("the cursor is pressing the left key")

    def writeCursorRigh(self):
        print("the cursor is pressing the right key")