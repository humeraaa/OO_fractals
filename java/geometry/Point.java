
package geometry;

// Class Point - represents a 2D point with x and y coordinates
public class Point {
    // === Fields (Attributes) ===
    private float x;  // X-coordinate
    private float y;  // Y-coordinate

    // === Default Constructor ===
    public Point() {
        this.x = 0;
        this.y = 0;
    }

    // === Parameterized Constructor ===
    public Point(float x, float y) {
        this.x = x;
        this.y = y;
    }

    // === Getter for X ===
    public float getX() {
        return x;
    }

    // === Setter for X ===
    public void setX(float x) {
        this.x = x;
    }

    // === Getter for Y ===
    public float getY() {
        return y;
    }

    // === Setter for Y ===
    public void setY(float y) {
        this.y = y;
    }

    // === Combined Setter for Both x and y ===
    // Demonstrates method overloading
    public void set(float x, float y) {
        this.x = x;
        this.y = y;
    }

    // === Add Two Points and Return a New One ===
    public Point add(Point other) {
        return new Point(this.x + other.x, this.y + other.y);
    }

    // === Override toString() for Better Print Output ===
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
