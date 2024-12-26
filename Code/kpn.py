from Detector import Detector
from Scroller import Scroller
class kpn: 
    def __init__(self):
        self.state = Detector(self)
        self.state.start()

    def setToAppState(self):
        self.state.stop()
        self.state = Scroller(self) 
        self.state.start()
    def setToDetectorState(self):
        self.state.stop()
        self.state = Detector(self)
        self.state.start()

context = kpn()