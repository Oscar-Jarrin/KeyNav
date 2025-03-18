from pynput.keyboard import Listener, Key
from InputProcessing.KeysToStrParser import KeysToStrParser

class InputTracker:
    def __init__(self):
        self.modifiersPressed = set()
        self.keysPressed = set()
        self.modifiers = {
            Key.alt,
            Key.alt_gr,
            Key.alt_l,
            Key.alt_r,
            Key.ctrl,
            Key.ctrl_l,
            Key.ctrl_r,
            Key.shift,
            Key.shift_l,
            Key.shift_r,
            Key.caps_lock,
        }
        self.keysToStr = KeysToStrParser()
        self.supressKeys = False
        self.listener = self.__createListener()

    def __createListener(self): 
        listener = Listener(on_press=self.handlePress, on_release=self.handleRelease, suppress = self.supressKeys)
        listener.start()            
        return listener
    
    def setKeyboardSupression(self, newSupressKeysValue: bool):
        if newSupressKeysValue != self.supressKeys:
            self.supressKeys = newSupressKeysValue
            if self.listener:
                self.listener.stop()
                self.listener.join()
            self.__resetKeysPressed()
            self.listener = self.__createListener()

    def handlePress(self, key):
        if key in self.modifiers:
            self.modifiersPressed.add(key)
        else:
            self.keysPressed.add(key)

    def handleRelease(self, key):
        #the elif is necessary because when I run it from the terminal, 
        #you press enter and the program starts
        #but when you release it, it tries to delete the enter key but the list is empty so it raises an exception
        if key in self.modifiers:
            self.modifiersPressed.discard(key)
        elif key in self.keysPressed:
            self.keysPressed.discard(key)
    
    def getCurrentKeySequences(self):
        combinationsPressed = set() #set of str formatted combinations
        localCombination = None #the combination detected for every modifiers*key
        formattedCombination = None #the str version of the combination detected
        for key in self.keysPressed:
            localCombination = list()
            for modifier in self.modifiersPressed:
                localCombination.append(modifier)
            localCombination.append(key)
            formattedCombination = self.keysToStr.formatSequence(localCombination)
            combinationsPressed.add(formattedCombination)
        return combinationsPressed

    def __resetKeysPressed(self):
        self.keysPressed.clear()
        self.modifiersPressed.clear()