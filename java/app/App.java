
//App.java becomes the control center.

package app;


import javax.swing.JFrame;


import geometry.Point;
import drawing.Pen;
import drawing.Canvas;




public class App {
    public void run() {
        System.out.println("Welcome to the OOP demonstration using the Point class.\n");

        // -- POINT DEMO --
        Point P = new Point(); 
        P.setX(5);
        P.setY(10);
        P.set(2, 3);
        Point Q = new Point(7, 4);
        Point R = P.add(Q);

        System.out.println("Point R = P + Q: " + R);
        System.out.println("X value of R: " + R.getX());
        System.out.println("Y value of R: " + R.getY());

        // -- PEN + CANVAS DEMO --
        Canvas canvas = new Canvas();
        Pen pen = new Pen(canvas);

        pen.moveTo(100, 100);
        pen.lineTo(200, 100);
        pen.lineTo(200, 200);
        pen.lineTo(100, 200);
        pen.lineTo(100, 100);

        JFrame frame = new JFrame("Humera Tariq Canvas");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.add(canvas);
        frame.setVisible(true);

        System.out.println("\nProgram completed successfully.");
    }
}
