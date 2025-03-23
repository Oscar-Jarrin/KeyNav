import time
from graphics.GUI import GUI
from InputProcessing.InputTracker import InputTracker
from states.MouseState import MouseSimulator
from states.TransparentState import TransparentMode

class KeyNav():
    def __init__(self):
        self.gui = GUI()
        self.mouseState = MouseSimulator(self, self.gui)
        self.transparentState = TransparentMode(self, self.gui)
        self.inputTracker = InputTracker()
        self.currentState = self.mouseState
        self.__startSimulation()
        self.running = True
    #maybe locate the inputTracker and the while loop here
    #and send the inputs to the state

    def __startSimulation(self):
        while True:
            currentCombinations = self.inputTracker.getCurrentKeySequences()
            self.currentState.handleCombinations(currentCombinations)
            time.sleep(0.02)            

    def setToTransparentMode(self):
        self.running = False
        self.currentState = self.transparentState
        self.inputTracker.setKeyboardSupression(False)
        self.running = True
        self.__startSimulation()
        print("context set to transparent mode")

    def setToMouseMode(self):
        self.running = False
        self.currentState = self.mouseState
        self.inputTracker.setKeyboardSupression(True)
        self.running = True
        self.__startSimulation()
        print("context set to mouse mode")