package drawing;

import geometry.Point;               // Your custom Point class
import java.awt.Graphics;           // For paintComponent
import javax.swing.JPanel;          // For extending JPanel
import java.util.ArrayList;         // For ArrayList
import java.util.List;              // For List interface

public class Canvas extends JPanel {
    
    static class Line {
        Point start, end;

        Line(Point s, Point e) {
            this.start = s;
            this.end = e;
        }
    }

    private List<Line> lines = new ArrayList<>();

    public void addLine(Point p1, Point p2) {
        lines.add(new Line(p1, p2));
        System.out.println("Line from (" + p1.getX() + ", " + p1.getY() +
                           ") to (" + p2.getX() + ", " + p2.getY() + ")");
        repaint(); // To trigger paintComponent and draw immediately
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (Line line : lines) {
            g.drawLine((int) line.start.getX(), (int) line.start.getY(),
                       (int) line.end.getX(), (int) line.end.getY());
        }
    }
}
