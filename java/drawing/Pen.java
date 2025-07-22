
package drawing;

import geometry.Point;

public class Pen {
    private Point CP;               // Current Position
    private Canvas cvs;   // Canvas to draw on

    public Pen(Canvas canva) {
        this.cvs = canva;
        this.CP = new Point(0, 0); // Start at origin
    }

    public void moveTo(float x, float y) {
        this.CP = new Point(x, y);
    }

    public void lineTo(float x, float y) {
        Point newPoint = new Point(x, y);
        cvs.addLine(this.CP, newPoint); // Draw line
        this.CP = newPoint; // Update current position
    }

    public Point getPosition() {
        return this.CP;
    }
}