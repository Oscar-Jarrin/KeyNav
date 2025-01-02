from pynput.keyboard import Listener 
from pynput.keyboard import Key, KeyCode
class Detector:
    def __init__(self, context):
        self.keys_queue = set()
        self.listener = None
        self.context = context

    def start(self): 
        keys_queue = self.keys_queue
        context = self.context
        print("the detector has started") 
        def press(key):             
            keys_queue.add(key)
            if(Key.alt_l in keys_queue and key == KeyCode.from_char('c')):
                context.setToAppState() #create the context class and add the settoappmode() method 
                print("alt + c was pressed") 

        def release(key):
            keys_queue.discard(key)
        self.listener = Listener(on_press=press, on_release=release, suppress=False)
        self.listener.start()

    def stop(self):
        self.listener.stop()









































































































