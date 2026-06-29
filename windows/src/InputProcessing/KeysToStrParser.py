from pynput.keyboard import Key, KeyCode 

class KeysToStrParser: 
    def __init__(self):
        #print("im in the KeysToStrParser builder")
        pass

    def formatSequence(self, keySequence: list):
        if not keySequence: #means if the list is empty
            return "all_keys_released"
        strOfFormatedKeys = "+".join([self.__formatKey(key) for key in keySequence]) 
        #here I swap the order of alt+ctrl so that the configurations can use the same
        #notation, but the user can press them in any order 
        if "alt+ctrl" in strOfFormatedKeys:
            strOfFormatedKeys = strOfFormatedKeys.replace('alt+ctrl', 'ctrl+alt') 
        return strOfFormatedKeys

    def __formatKey(self, key):
            #I also format alt_gr as alt because when this key is pressed,
            #for some reason I don't know, the system thinks both ctrl and alt_gr were pressed
            #so as the behaviour of ctrl+alt is almost the same, I just format it as alt
            #and the returned formatted sequence is ctr+alt which is the notation I use for
            #the configuration of special characters in the specialCharactersConfig map inside WriteMode
            toRet = None
            if key == Key.alt_l or key == Key.alt_r or key == Key.alt_gr: 
                toRet = "alt"
            elif key == Key.shift_l or key == Key.shift_r:
                toRet = "shift"
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                toRet = "ctrl"
            elif key == Key.space:
                toRet = "space_bar"
            elif hasattr(key, "name"):
                toRet = key.name
            elif isinstance(key, Key): 
                toRet = key.name
            elif isinstance(key, KeyCode):
                toRet = key.char
            if toRet is None:
                toRet = "NonRecognizedChar"
            return toRet