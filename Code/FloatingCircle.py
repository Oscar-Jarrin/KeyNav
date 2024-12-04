import tkinter as tk
import ctypes

class FloatingCircumference:
    def __init__(self, radius=80, color="blue", thickness=3):
        self.radius = radius
        self.root = tk.Tk()
        
        # Window configuration: remove title bar, set transparency and keep on top
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.wm_attributes('-transparentcolor', 'white')  # Transparent background

        # Configure the canvas for the circumference
        self.canvas = tk.Canvas(self.root, width=2*radius, height=2*radius, bg='white', highlightthickness=0)
        self.canvas.pack()
        self.canvas.create_oval(
            thickness, thickness, 2*radius - thickness, 2*radius - thickness,
            outline=color, width=thickness
        )

        # Center window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 2*radius) // 2
        y = (screen_height - 2*radius) // 2
        self.root.geometry(f"{2*radius}x{2*radius}+{x}+{y}")

    def run(self):
        self.root.mainloop()

# Adjust DPI settings for high-resolution screens on Windows
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Run the program with a desired radius and color
floating_circumference = FloatingCircumference(radius=100, color="blue", thickness=4)
floating_circumference.run()
