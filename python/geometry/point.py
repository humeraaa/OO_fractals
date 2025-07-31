# geometry/point.py

class Point:
    """
    A 2D Point class to demonstrate Python OOP:
    - Instance attributes
    - Constructors (__init__)
    - Encapsulation (with property decorators)
    - Method overloading (simulated)
    - Operator overloading
    - String representation (__str__)
    - Class variable, static method, class method
    """

    # === Class variable ===
    count = 0  # Tracks number of Point instances

    def __init__(self, x=0.0, y=0.0): #Default values are only used if the caller does not provide arguments.
        """
        A flexible constructor that simulates:
        1. Default constructor           --> Point()
        2. Parameterized constructor     --> Point(x, y)
        3. Copy constructor              --> Point(Point_obj)

        Parameters:
        - x: float OR another Point object
        - y: float (ignored if x is a Point)
        """
        if isinstance(x, Point):
            # Copy constructor logic (like: this.x = other.x in Java)
            self._x = x._x
            self._y = x._y
            print("Copy constructor logic invoked")
        else:
            self._x = x
            self._y = y

        Point.count += 1

    # === Properties (Getters and Setters) ===
    # The underscore-prefixed _x is the private storage.
    # The property x is the official interface to access or mutate it.
    # @property
    # def x(self):
    #     return self._x

    # @x.setter
    # def x(self, value):
    #     self._x = value

    # @property
    # def y(self):
    #     return self._y

    # @y.setter
    # def y(self, value):
    #     self._y = value

    #To reuse property logic inside set(), just assign like self.x = x instead of self._x = x.
    #This way, you're not duplicating logic — you're delegating it to the proper setter.    
    #Why we emphasize using the setter (self.x = x) instead of direct attribute access (self._x = x)?
    # Because this ensures all value assignments go through one unified gate — the x.setter.
    # That means:
    # Validation is enforced
    # Future logic (e.g., event firing, logging, bounds checking) is respected
    # Less duplication (you don’t write the same isinstance check everywhere)
    # def set(self, x=None, y=None):
    #     if x is not None:
    #         self.x = x  # Uses the @x.setter
    #     if y is not None:
    #         self.y = y  # Uses the @y.setter


    # --- Java-style getter/setter ---
    def get_x(self):
        return self._x

    def set_x(self, value):
        print("Setting x via java style method")
        self._x = value        
    
    def set_y(self, value):
        print("Setting y via java style method")
        self._y = value        

    def get_x(self):
        return self._x

    def get_y(self):  
        return self._y

    # === Method to add two points ===
    def add(self, other):
        """Add two Point objects and return a new one"""
        if isinstance(other, Point):
            return Point(self._x + other._x, self._y + other._y)
        raise TypeError("Can only add Point to Point")

    # === Operator overloading for + ===
    def __add__(self, other):
        return self.add(other)

    # === String representation ===
    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Point(x={self._x}, y={self._y})"

    # === Equality override ===
    def __eq__(self, other):
        return isinstance(other, Point) and self._x == other._x and self._y == other._y

    def distance(self, p):
        return ((self._x - p._x)**2 + (self._y - p._y)**2)**0.5
    
    # === Class method to get total instances ===
    @classmethod
    def get_instance_count(cls):
        return cls.count

    
