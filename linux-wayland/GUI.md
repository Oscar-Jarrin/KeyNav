# HUD (head-up display)
> the visibility of this HUD can be toggled in case it is bugging the user, or maybe configure the information it can display

### Current State
- Display information about the current state {Mouse, Vim (Control, Select), Transparent}
0. In a side bar (which place can be configured), show maybe a contraction like [sel], [ctrl], [mouse], [transparent]. And maby a small figure or image

### Mouse Binds 
- Display the current binds (sequence/chain) being recognized
1. Configure binds for:
  - for each mouse button: (left, right, middle)
    - Basic click
    - Click and hold
    - Unclick/Release
> This can be modeled with a graph (when the bind tracker in the Keynav module sends the event of a new bind member is added)

> left button bind:
>        | _______________________   _____________             
>        |                         \              \
> basic click bind (default) | hold bind | release bind | 

### Current Zone Indication
- Display the change in zones
2. Cursor Mobility Functionalities
  - Zones Mobility
    - Dive into zone (x, y) | {x, y e 3x3 grid}
    - Arise to previous zone 
    - Reset to full-screen zone
> It can be like a glass grid of the current state

# Configuration HUB (gui to configure binds)

### Transparent State
0. Configure binds to change to all other modes
1. Configure binds to peek to all other modes
2. Configure binds for delete a word 
3. Configure binds for delete a char

### Vim Control State
0. Configure binds for change to all other modes
1. Configure binds for peek to all other modes
2. Configure binds for every **TextBlock**
3. Configure binds for every **Verbs**
4. Configure binds for every **Action**

### Vim Select State
0. Configure binds for change to all other modes
1. Configure binds for peek to all other modes
2. Configure binds for every **TextBlock**
3. Configure binds for every **Verbs**
4. Configure binds for every **Action**

### Mouse State
0. Configure binds for change to all other modes
1. Configure binds for peek to all other modes
2. Configure mouse movement basic speed
3. Configure mouse speed increment speed
4. Configure binds for default spots
