from Scroller import Scroller
from Detector import Detector
from threading import Event
class kpn: 
    def __init__(self):
        self.state = Detector(self)
        self.state.start()
        print("The kpn has been created")
    def setToAppState(self):
        print("kpn is in scroll mode")
        self.state.stop()
        self.state = Scroller(self) 
        self.state.start()
    def setToDetectorState(self):
        print("kpn is in detector mode")
        self.state.stop()
        self.state = Detector(self)
        self.state.start()

context = kpn()
Event().wait()