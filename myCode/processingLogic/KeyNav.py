from hardwareControllers.HwManager import  HwManager
from graphics.GUI import GUI
from states.MouseMode import MouseMode 
from states.TransparentMode import TransparentMode
from states.WriteMode import WriteMode
from states.SwapMode import SwapMode 
from pynput.keyboard import Key as pynputKey

class KeyNav: 
    def __init__(self):
        #by default, the KeyNav is initialized in TransparentMode
        self.state = MouseMode(self)
        #TransparentMode(self) 
        self.hw = HwManager() 
        self.gui = GUI()
        self.lastState = None

    def handleInput(self, keySequence: list):
        formatedSequence = self.__formatSequence(keySequence)
        #print(formatedSequence)
        self.state.handleInput(formatedSequence)

    def __formatSequence(self, keySequence: list):
        if not keySequence: #means if the list is empty
            return "all_keys_released"
        formatedSequence = "+".join(self.__formatKey(key) for key in keySequence) 
        #here I swpa the order of alt+ctrl so that the configurations can use the same
        #notation, but the user can press them in any order 
        if "alt+ctrl" in formatedSequence:
            formatedSequence = formatedSequence.replace('alt+ctrl', 'ctrl+alt') 
        return formatedSequence

    def __formatKey(self, key) -> str:
            #I also format alt_gr as alt because when this key is pressed,
            #for some reason I don't know, the system thinks both ctrl and alt_gr were pressed
            #so as the behaviour of ctrl+alt is almost the same, I just format it as alt
            #and the returned formatted sequence is ctr+alt which is the notation I use for
            #the configuration of special characters in the specialCharactersConfig map inside WriteMode
            if key == pynputKey.alt_l or key == pynputKey.alt_r or key == pynputKey.alt_gr: 
                return "alt"
            elif key == pynputKey.shift_l or key == pynputKey.shift_r:
                return  "shift"
            elif key == pynputKey.ctrl_l or key == pynputKey.ctrl_r:
                return "ctrl"
            elif key == pynputKey.space:
                return "space_bar"
            elif hasattr(key, "name"):
                return key.name
            else:
                return key.char

    def setToTransparentMode(self):
        print("keynav to transparent")
        self.state = TransparentMode(self)

    def setToWriteMode(self):
        print("keynav to write")
        self.state = WriteMode(self)

    def setToMouseMode(self):
        print("keynav to mouse")
        self.state = MouseMode(self)

    def setToSwapMode(self):
        print("keynav to swap")
        self.lastState = self.state
        self.state = SwapMode(self) 

    def getHwController(self):
        return self.hw
    
    def setToPreviousMode(self):
        print("keynav to previous")
        self.state = self.lastState
        
    def getGUI(self):
        return self.gui