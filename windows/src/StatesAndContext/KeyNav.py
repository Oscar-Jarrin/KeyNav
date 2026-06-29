import time
from graphics.GUI import GUI
from InputProcessing.InputTracker import InputTracker
from StatesAndContext.MouseState import MouseSimulator
from StatesAndContext.TransparentState import TransparentMode

class KeyNav():
    def __init__(self):
        self.running = True
        self.gui = GUI()
        self.mouseState = MouseSimulator(self, self.gui)
        self.transparentState = TransparentMode(self, self.gui)
        self.inputTracker = InputTracker()
        self.currentState = self.transparentState

        self.__startSimulation()

    def __startSimulation(self):
        #print("im restarting the main while in keynav ")
        while self.running:
            #print(f"the alt key is being pressed: {keyboard.is_pressed('alt')}")
            currentCombinations = self.inputTracker.getCurrentKeySequences()
            self.currentState.handleCombinations(currentCombinations)
            time.sleep(0.03)            

    def setToTransparentMode(self):
        #print("Im bout to go from mouse to transparentMode")
        self.running = False
        self.inputTracker.setKeyboardSupression(False)
        self.running = True
        self.currentState = self.transparentState
        self.__startSimulation()
        #print("context set to transparent mode")

    def setToMouseMode(self):
        #print("im bout to go from transparent to mouseMode")
        self.running = False
        self.inputTracker.setKeyboardSupression(True)
        self.running = True
        self.currentState = self.mouseState
        self.__startSimulation()
        #print("context set to mouse mode")
    