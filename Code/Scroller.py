from pynput.keyboard import Listener, Key, KeyCode
from pynput.mouse import Controller

class Scroller:
    def __init__(self, context):
        self.keys_queue = set()
        self.listener = None
        self.context = context 
        self.mouse = Controller() 
        print("the scroller has been created")
    def start(self):
        keys_queue = self.keys_queue
        context = self.context
        mouse = self.mouse
        def press(key):
            keys_queue.add(key)
            if(Key.alt_l in keys_queue and key == KeyCode.from_char('c')):
                print("alt + c was pressed")
                context.setToDetectorState() #CREATE THE CONTEXT CLASS AND ADD THE SETMANAGERSTATE() METHOD
        print("the scroller has started")
        def release(key):
            if key == Key.media_volume_up or key == KeyCode.from_char('k'):
                print("scroll up")
                mouse.scroll(0,1) 
            elif key == Key.media_volume_down or key == KeyCode.from_char('j'):
                print("scroll down")
                mouse.scroll(0, -1) 
            keys_queue.discard(key)

        self.listener = Listener(on_press=press, on_release=release, suppress=True)
        self.listener.start()
        
    def stop(self):
        self.listener.stop()