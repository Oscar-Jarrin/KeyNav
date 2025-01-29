import sys
import processingLogic.KeyNav as kn
import processingLogic.InputManager as im
from threading import Event
from pynput.keyboard import Controller, Key
import time

#time.sleep(3)
#keyboar = Controller()
#keyboar.press(Key.alt)
#keyboar.press(Key.tab)
#keyboar.release(Key.alt)
#keyboar.release(Key.tab)

k = kn.KeyNav()
im = im.InputManager(k) 
#print(sys.path)
Event().wait()
#print(sys.prefix )
#print(sys.base_prefix)
