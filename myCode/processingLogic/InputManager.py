from pynput.keyboard import Listener 
from processingLogic.KeysToStrParser import KeysToStrParser

class InputManager:
    def __init__(self, mouseSimulator):
        #print("im in the InputManager builder")
        self.keysToStr = KeysToStrParser()
        self.keySecuence = list()
        self.mouseSimulator = mouseSimulator
        self.listener = self.__createListener()

    def __createListener(self): 
        listener = Listener(on_press=self.handlePress, on_release=self.handleRelease, suppress = True)
        listener.start()            
        return listener

    def handlePress(self, key):
        if not key in self.keySecuence:
            self.keySecuence.append(key) 
        #notify the mouseMode
        commandPressed = self.keysToStr.formatSequence(self.keySecuence)
        self.mouseSimulator.simulateOn(commandPressed)

    def handleRelease(self, Key):
        #this one is necessary because when I run it from the terminal, 
        #you press enter and the program starts
        #but when you release it, it tries to delete the enter key but the list is empty so it raises an exception
        if(Key in self.keySecuence): 
            self.keySecuence.remove(Key)
        if not self.keySecuence: #notifies the "all keys released"
            commandPressed = self.keysToStr.formatSequence(self.keySecuence)
            self.mouseSimulator.simulateOn(commandPressed)