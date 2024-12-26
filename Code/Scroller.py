from pynput.keyboard import Listener, Key, KeyCode
from pynput.mouse import Controller

class Scroller:
    def __init__(self, context):
        self.keys_queue = set()
        self.listener = None
        self.context = context 
        self.mouse = Controller() 

    def start(self):
        keys_queue = self.keys_queue
        context = self.context
        mouse = self.mouse
        def press(key):
            keys_queue.add(key)

        def release(key):
            if(Key.alt_l in keys_queue and key == KeyCode.from_char('c')):
                print("alt + c was pressed")
                context.setDetectorState() #CREATE THE CONTEXT CLASS AND ADD THE SETMANAGERSTATE() METHOD
            if (Key.ctrl_l in keys_queue):
                if key == Key.media_volume_up:
                    print("scroll up")
                    mouse.scroll(0,3) 
                elif key == Key.media_volume_down:
                    print("scroll down")
                    mouse.scroll(0, -3) 
            if key == Key.esc:
                return False
            keys_queue.discard(key)

        self.listener = Listener(on_press=press, on_release=release, suppress=True)
        self.listener.start()
        
    def stop(self):
        self.listener.stop()