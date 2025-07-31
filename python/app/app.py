
#Make sure drawing/ and geometry/ both have an __init__.py file (can be empty) to mark them as Python packages.
#In Python: file/module names should be lowercase and must match in your import exactly.
# file name like Canvas is valid on Windows, but breaks imports on Linux/Mac.


import tkinter as tk
from geometry.line import Line  # Assuming you have a Line class defined in geometry module
from geometry.point import Point  # Assuming you have a Point class defined in geometry module
from drawing.canvas import TKpanel
from drawing.pen import Pen  # Assuming you have a Pen class defined in drawing module


class App:
    def __init__(self):
        self.root = tk.Tk()     # calling parent/super/base class constructor like JFrame
        self.root.title("Humera Tariq Canvas")
        self.canvas = TKpanel(self.root, width=400, height=400)
        self.canvas.pack()

    def run(self):
        print("Welcome to the OOP demonstration using the Point class.\n")

        # -- POINT DEMO --
        P = Point()
        P.set_x(5)
        P.set_y(10)
        P.set_x(2)
        P.set_y(3)
        Q = Point(7, 4)
        R = P + Q  # Uses __add__

        print("Point R = P + Q:", R)
        print("X value of R:", R.get_x())
        print("Y value of R:", R.get_y())

        # -- PEN + CANVAS DEMO --
        pen = Pen(self.canvas)
        pen.move_to(100, 100)
        pen.line_to(200, 100)
        pen.line_to(200, 200)
        pen.line_to(100, 200)
        pen.line_to(100, 100)

        print("\nProgram completed successfully.")
        self.root.mainloop()     # It is like frame.setVisible(true) in Java


