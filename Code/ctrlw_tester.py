from pynput.keyboard import Listener, Key

keys_quee = set()

def instructionShortcutsListener(key):
    keys_quee.add(key)

def instructionShorcutExit(key):
    keys_quee.discard(key)
    if key == Key.esc:
        return False
    if key == Key.media_volume_up:
        print("volume up")
with Listener(on_press=instructionShortcutsListener, on_release=instructionShorcutExit, suppress=True) as listener: 
    listener.join()
