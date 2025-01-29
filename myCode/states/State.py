from abc import ABC, abstractmethod
import processingLogic.KeyNav as KeyNav
from configparser import ConfigParser
from . import State

class State(ABC):
    def contextToSwapMode(self):
        self.context.setToSwapMode()
        
    @abstractmethod
    def handleInput(keySequence: str):
        pass
    