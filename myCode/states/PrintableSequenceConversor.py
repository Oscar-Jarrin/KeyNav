from difflib import SequenceMatcher
class PrintableSequenceConversor():
    def __init__(self):
        self.lastWrittenString = "" 
        self.muteKeys = [
            "esc",
            "tab",
            "ctrl",
            "alt",
            "menu",
            "ctr+alt",
            "f1",
            "f2",
            "f3",
            "f4",
            "f5",
            "f6",
            "f7",
            "f8",
            "f9",
            "f10",
            "f11",
            "f12",
            "up",
            "down",
            "right",
            "left",
            "caps_lock",
            "cmd",
            "ctrlalt"
        ]
        self.specialCharactersConfig = {
            #"|":"|",
            "enter": "\n",
            "shift+|":"°",
            "ctrl+alt+|":"¬",
            "shift+1":"!",
            'shift+2':'"',
            "shift+3":"#",
            "shift+4":"$",
            "shift+5":"%",
            "shift+6":"&",
            "shift+7":"/",
            "shift+8":"(",
            "shift+9":")",
            "shift+0":"=",
            #"'":"'",
            "shift+'":"?",
            "ctrl+alt+'":"\\", #this represents \ but I need to scape it with a \\
            #"¿":"¿",
            "shift+¿":"¡",
            #"´":"´",
            "shift+´":"¨",
            #"+":"+",
            "shift++":"*",
            "ctrl+alt++":"~",
            #"{":"{",
            "shift+{":"[",
            "ctrl+alt+{":"^",
            #"}":"}",
            "shift+}":"]",
            "ctrl+alt+}":"`",
            #"<":"<",
            "shift+<":">",
            #",":",",
            "shift+,":";",
            #".":".",
            "shift+.":":",
            #"-":"-",
            "shift+-":"_",
            #"ñ":"ñ",
            "ctrl+alt+q":"@",
            "space_bar": " "
        }

    def transformToPrintableSequence(self, keySequence: str):
        keySequence = self.__interpretKeySequence(keySequence)
        textWithoutGhostKeys = self.__antiGhostSequence(keySequence)
        return textWithoutGhostKeys 


    def __interpretKeySequence(self, keySequence: str):
        keySequence = self.__removeSpecialStrings(keySequence)
        listWithoutPlus = self.__deletePlus(keySequence)
        listWithoutExtraKeys = self.__deleteExtraKeys(listWithoutPlus)
        readyToPrintList = self.__interpretShifts(listWithoutExtraKeys) 
        printableString = "".join(readyToPrintList)
        return printableString 

    def __removeSpecialStrings(self, keySequence: str):
        for specialSequence in self.specialCharactersConfig:
            if specialSequence in keySequence:
                keySequence = keySequence.replace(specialSequence, self.specialCharactersConfig[specialSequence]) 
        return keySequence

    def __deletePlus(self, sequenceWithPlus: str):
        sequenceWithoutPlus = sequenceWithPlus.split("+")
        currentElem = 0
        plusReplaced = 0
        while currentElem < len(sequenceWithoutPlus) - 1 - plusReplaced:
            if sequenceWithoutPlus[currentElem] == "" and sequenceWithoutPlus[currentElem + 1] == "": 
                sequenceWithoutPlus[currentElem] = "+"
                del sequenceWithoutPlus[currentElem + 1]
                plusReplaced = plusReplaced+1
            currentElem = currentElem+1
        return sequenceWithoutPlus
    
    def __deleteExtraKeys(self, listOfKeys):
        for key in listOfKeys:
            if key in self.muteKeys:
                listOfKeys.remove(key)
        return listOfKeys

    def __interpretShifts(self, listOfKey):
        shiftPressed = False
        i = 0
        while i < len(listOfKey) and not shiftPressed:
            shiftPressed = listOfKey[i] == "shift"
            i = i+1 
        while i < len(listOfKey) and shiftPressed:
            if listOfKey[i].isalpha() and shiftPressed:
                listOfKey[i] = listOfKey[i].upper()
            i = i + 1
        if "shift" in listOfKey:
            listOfKey.remove("shift")
        return listOfKey 
                

    def __antiGhostSequence(self, keySequence: str):
        if keySequence == "all_keys_released" or keySequence == "space_bar":
            self.lastWrittenString = ""
            return ""
        charsDeleted = 0
        if self.lastWrittenString == "":
           self.lastWrittenString += keySequence
           return keySequence 
        intersection = self.__findMatchingSubsequence(keySequence, self.lastWrittenString) 
        for char in intersection:
            keySequence = keySequence.replace(char, "", 1)
        self.lastWrittenString += keySequence
        return  keySequence 

    def __findMatchingSubsequence(self, keysequence, lastWrittenString):
        seqFinder = SequenceMatcher(None, keysequence, lastWrittenString)
        match = seqFinder.find_longest_match(0, len(keysequence), 0, len(lastWrittenString))
        return keysequence[match.a: match.a + match.size]