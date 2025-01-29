from pynput.keyboard import Listener, Key as pynputKey
from threading import Event 

class InputManager:
    def __init__(self, keyNav):
        self.kn = keyNav
        self.keySecuence = list()
        self.listener = self.__createListener()

    def handlePress(self, key):
        if not key in self.keySecuence:
            self.keySecuence.append(key) 
        self.kn.handleInput(self.keySecuence)

    def handleRelease(self, Key):
        if(Key in self.keySecuence): 
            #this one is necessary because when I run it from the terminal, 
            #you press enter and the program starts
            #but when you release it, it tries to delete the enter key but the list is empty so it raises an exception
            self.keySecuence.remove(Key)
        if not self.keySecuence:
            self.kn.handleInput(self.keySecuence)

    def __createListener(self) -> Listener:
        listener = Listener(on_press=self.handlePress, on_release=self.handleRelease, suppress=True)
        listener.start()            
        return listener