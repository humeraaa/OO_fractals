from geometry.point import Point  # Adjust import as per your folder structure

class Pen:
    """
    A Pen class that mimics drawing behavior:
    - Maintains a current position (CP)
    - Interfaces with a Canvas object to draw lines
    """

    def __init__(self, canvas):
        """
        Initializes the pen with a canvas to draw on.
        Starts at origin (0, 0).
        """
        self._canvas = canvas     # Assumed to have an add_line(Point, Point) method
        self._cp = Point(0, 0)    # Current position

    def move_to(self, x, y):
        """
        Moves the pen to a new position without drawing.
        """
        self._cp = Point(x, y)

    def line_to(self, x, y):
        """
        Draws a line from the current position to the new point.
        Updates current position afterward.
        """
        new_point = Point(x, y)
        self._canvas.add_line(self._cp, new_point)
        self._cp = new_point

    def get_position(self):
        """
        Returns the current position of the pen.
        """
        return self._cp
