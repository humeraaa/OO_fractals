# main.py
# Demonstrating constructor, setters, getters, and object printing from Point class

from geometry.Point import Point
import copy

def main():
    # --- Constructor Calls: Java vs Python Comparison ---

    # Equivalent to: Point p1 = new Point(3, 4); in Java
    p1 = Point(3, 4)
    print("p1 =", p1)

    # Equivalent to: Point p2 = new Point(); in Java
    p2 = Point()
    print("p2 =", p2)

    # Equivalent to: Point p3 = new Point(p1); in Java (copy constructor)
    p3 = Point(p1)
    print("p3 (copy of p1) =", p3)

    print("Total Point instances created:", Point.count)

    # --- Using setters to modify values ---
    p2.set_x(10)
    p2.set_y(20)

    # --- Using getters to retrieve values ---
    print("p1 coordinates:", p1.get_x(), ",", p1.get_y())
    print("p2 coordinates:", p2.get_x(), ",", p2.get_y())

    # --- Printing object directly (uses __str__) ---
    print("Object p1 (user-friendly):", p1)       # Calls __str__
    print("Object p2 (developer view):", repr(p2))  # Calls __repr__

    # Optional: Show that str() and repr() can also be called explicitly
    print("str(p1):", str(p1))
    print("repr(p2):", repr(p2))

    print("---------------------- Week 04  copying reference vs copying object ----------------------")
    
    # Object Assignment or shallow copy
    #does not copy anything; it just makes p2 point to the same object as p1
    #This is a name binding, not an operation on the object.
    #Python's philosophy is that names are just labels for objects, and rebinding a label should be simple and predictable.
    p2= p1     
    print("after assignment confusion :)")    
    print(p2)

    p2=p1=p3  # All three variables now refer to the same Point object
    print("After p2=p1=p3, p2 =", p2)
    print("====================================================================")
    
    
    # You need p2.__dict__ to see the attributes specially when pythonic @property design is not used
    # With out @property we are in trouble as python interpreter add an extra attribute without informing us
    #{'_x': 3, '_y': 4, 'x': 100}
    p2 = p1
    p2.x = 100
    print("Assignment: p1 =", p1, "| p2 =", p2)  # both change
    print("Confused face: ","---(:)-----")  # May still raise encoding issue in some consoles
    print(p2.__dict__)  # To see what attributes exist on p2 when pythonic @property design was not used

    
    





# This block ensures main() runs only if this file is executed directly
if __name__ == "__main__":
    main()