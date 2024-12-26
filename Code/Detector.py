from pynput.keyboard import Listener, Key, KeyCode

class Detector:
    def __init__(self, context):
        self.keys_queue = set()
        self.listener = None
        self.context = context

    def start(self): 
        keys_queue = self.keys_queue
        context = self.context

        def press(key):             
            keys_queue.add(key)

        def release(key):
            if(Key.alt_l in keys_queue and key == KeyCode.from_char('c')):
                context.setToAppState() #CREATE THE CONTEXT CLASS AND ADD THE SETTOAPPMODE() METHOD 
                print("alt + c was pressed") 
            if key == Key.esc: 
                return False 
            keys_queue.discard(key)
        self.listener = Listener(on_press=press, on_release=release, suppress=False)
        self.listener.start()

    def stop(self):
        self.listener.stop()









































































































