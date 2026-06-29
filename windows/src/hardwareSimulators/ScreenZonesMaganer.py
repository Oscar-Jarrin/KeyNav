import tkinter as tk

class ScreenZonesManager():
    def __init__(self):
        #I use tk to obtain the width and height of the screen 
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        root.destroy()
        self.defaultWidth = self.width
        self.defaultHeight = self.height

        #The initial point of the screen is (0,0) by default
        self.initial_x = 0
        self.initial_y = 0
        self.dx = self.width/3
        self.dy = self.height/3
        #print("the zones manager has been correctly created")

    def selectSubZone(self, xCoordinate, yCoordinate): 
        #I get the new values just for the sake of legibility
        #I'm well aware I could do this way more simply
        #print(f"the selectSubZone recieved {xCoordinate, yCoordinate}")
        newInitial_x = self.initial_x + yCoordinate*self.dx
        newInitial_y = self.initial_y + xCoordinate*self.dy
        newWidth = self.dx
        newHeight = self.dy
        newDx = self.dx/3
        newDy = self.dy/3
        newMouseCoordinateX = newInitial_x + self.dx/2 
        newMouseCoordinateY = newInitial_y + self.dy/2
        #update the new values 
        self.initial_x = newInitial_x
        self.initial_y = newInitial_y
        self.dx = newDx
        self.dy = newDy
        self.width = newWidth
        self.height = newHeight
        return newMouseCoordinateX, newMouseCoordinateY

    def resetZoneToScreen(self):
        self.height = self.defaultHeight        
        self.width = self.defaultWidth
        self.initial_x = 0
        self.initial_y = 0
        self.dx = self.defaultWidth/3
        self.dy = self.defaultHeight/3
        newMouseX = self.defaultWidth/2
        newMouseY = self.defaultHeight/2
        return newMouseX, newMouseY