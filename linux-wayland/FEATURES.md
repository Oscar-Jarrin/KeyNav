# KeyNav - Linux Keyboard-to-Mouse Navigation

# Across all modes Functionalities
- Peak at other modes modes
> maybe with the super Key

- Switch to all the different modes

# Transparent State Functions
> Across all modes Functionalities

- (Passive) Replicate all the keys pressed
> this mode sends the exact keyboard events it receives

# Mouse State Functions
> Across all modes Functionalities

- Mouse Clicks functionalities
  - **Modifier Keys** can be combined with clicks, for different application-specific needs
  > therefore the Modifier Keys cannot belong to a bind for any click

  - for each mouse button : (left, right, middle)
    - Basic click
    - Click and hold
    - Unclick/Release
    - Click DRAG Drop
    > DRAG: cursor Mobility Functionalities

- Cursor Mobility Functionalities
  - Zones Mobility
    - Dive into zone (x, y) | {x, y e 3x3 grid}
    - Arise to zone (x, y) | {x, y e 3x3 grid}
    - Reset to full-screen zone
  
  - Detailed Mobility
    - move along the four axis
    - Increase movement speed
    - Decrease movement speed

  - Deafult spots
    - be able to create binds (not belonging to existing commands) to a certain spot

- Scroll functionalities (chain of commands)
  - Scroll vertically/horizontally
  - Increase scroll speed
  - Decrease scroll speed

# Vim Type State Functionalities
> Initially, I believed that this would be like a transparent mode, that allows you to use binds like Alt+<keyBind> for certain actions
> But the magnitude of actions that one can do while managing text, demands a mode of its own.
> In this model, the insert mode there's in vim, can be simulated here by using the transparent mode. 

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
  > The select mode can de/activated using the v key, which would be implemented as just pressing the shift and just accepting TEXT_BLOCK events as input

# Vim Select State Grammar
TEXT_BLOCK = {number} + TextBlock
ACTION = TEXT_BLOCK | yank

**TextBlock**
  - word
  - begin of word (backwards)
  - end of word (forwards)
  - direction (all 4 directions)
  - go (start/end of line)

# Vim Controsl State Grammar
TEXT_BLOCK = {number} + TextBlock
VERB = {count} + terminalVerb
ACTION = {VERB} + TEXT_BLOCK

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