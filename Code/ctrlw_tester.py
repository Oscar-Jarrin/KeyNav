from pynput.keyboard import Listener, Key

keys_quee = set()

def instructionShortcutsListener(key):
    keys_quee.add(key)
    print(f"{key} was pressed")

    if Key.f in keys_quee and (key == 'w' or key.char == 'w'):
        print("Ctrl + W was pressed!")

def instructionShorcutExit(key):
    keys_quee.discard(key)
    if key == Key.esc:
        return False

with Listener(on_press=instructionShortcutsListener, on_release=instructionShorcutExit) as listener: 
    listener.join()
