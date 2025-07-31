import tkinter as tk
from geometry.point import Point  # Assuming you have a Point class defined in geometry module
from geometry.line import Line  # Your existing Point class

class TKpanel(tk.Canvas):
    def __init__(self, master=None, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)
        self.lines = []

    def add_line(self, p1: Point, p2: Point):
        """Adds a line and triggers drawing"""
        self.lines.append(Line(p1, p2))
        print(f"Line from ({p1.get_x()}, {p1.get_y()}) to ({p2.get_x()}, {p2.get_y()})")
        self.draw()  # Mimic Java's repaint()

    def draw(self):
        """Draw all stored lines"""
        self.delete("all")  # Clear previous drawings
        for line in self.lines:
            self.create_line(line.start.get_x(), line.start.get_y(),
                             line.end.get_x(), line.end.get_y(),
                             fill='black', width=2)
