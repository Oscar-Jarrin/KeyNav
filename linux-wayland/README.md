# KeyNav - Linux Keyboard-to-Mouse Navigation

# Transparent State Functions
- switch between different modes

# Across all modes Functionalities
- Peak at other modes modes
> maybe with the super Key

# Mouse State Functions
- Mouse Clicks functionalities (chain of commands)
  - **Modifier Keys** can be combined with certain clicks (they cannot be considered as part of a chain of commands)
  - for Each button: {left, right, middle}
    - Basic click
    - Click and hold
    - Unclick/Release
    - Clich Drag and Drop

- Scroll functionalities (chain of commands)
  - Scroll vertically/horizontally
  - Increase scroll speed
  - Decrease scroll speed
  
- Cursor Mobility Functionalities
  - Zones Mobility
    - Dive into zone (x, y) | {x, y e 3x3 grid}
    - Arise to zone (x, y) | {x, y e 3x3 grid}
    - Reset zone 
  
  - Detailed Mobility
    - move along the four axis
    - Increase movement speed
    - Decrease movement speed

  - Deafult spots
    - be able to bind keys to a certain spot

# Vim Type State Functionalities
- **Initially, I believe that this will be like a transparent mode, that allows you to use binds like Alt + <keyBind> for certain actions**
- **But now I am thinking it can be a mode of its own, where the insert mode is the transparent mode**

  - Delete a word forwards d+w
  - Delete a word backwards d+b

  - paste word in cursor place shift+p, P?
  - paste word after cursor place p

  - paste line above shift+p, P?
  - paste line beneath p

  - move a word forwards b
  - move a word backwards p

  - delete line forwards shift+d, D?
  - delete line backwards d0

  - move a line up k
  - move a line down j
  - move a character right l
  - move a character left h

  - go to end of the line g_, g+(shift-)
  - go to start of the line g0

  - go to end of the line and insert shift+a, A?
  - go to start of the line and insert shift+i, I?

  - start inserting on left of current character a
  - start inserting on right of current character i

  - yank line above  yk
  - yank line beneath yj
  - yank word forwards yw
  - yank word backwards yb

  - create a new line above shift+o, O?
  - create a new line below o

  - activate selection v
  - deactivate selection v
  > note: this is not another mode it is kind of a peek to a selection mode, because you can still use all the other commands above

  - if the first input is a number, then it represents the times that the next command will be executed
  > note:  vim grammar accepts count+command+noun as well

# Vim Type State Grammars
TEXT_BLOCK = {number} + terminalNoun
VERB = {count} + terminalVerb
ACTION = {VERB} + TEXT_BLOCK

| count + verb + textBlock
| verb + count + textBlock

**TextBlock**
  - word
  - begin of word (backwards)
  - end of word (forwards)
  - direction (all 4 directions)
  - go (start/end of line)

**Verbs**
  - non terminal
    - delete
    - yank

  - terminal
    - create line
    - paste (in after place)
    - activate/deactivate selection

# Glossary
- **Modifier Keys**: keys including ctrl, shift, alt, meta