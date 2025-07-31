from geometry.point import Point

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length(self):
        return self.start.distance(self.end)

    def __str__(self):
        return f"Line({self.start} → {self.end})"
