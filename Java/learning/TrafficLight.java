import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 * TrafficLight
 */
public class TrafficLight extends JFrame implements ActionListener {
    private JButton red, yellow, green;
    public TrafficLight() {
        setTitle("Traffic Light");
        setSize(500, 200);
        setLayout(new GridBagLayout());

        red = new JButton("RED");
        red.setBackground(Color.RED);
        red.setPreferredSize(new Dimension(100,50));
        yellow = new JButton("YELLOW");
        yellow.setBackground(Color.YELLOW);
        yellow.setPreferredSize(new Dimension(100,50));
        green = new JButton("GREEN");
        green.setBackground(Color.GREEN);
        green.setPreferredSize(new Dimension(100,50));

        add(red);
        add(yellow);
        add(green);

        red.addActionListener(this);
        yellow.addActionListener(this);
        green.addActionListener(this);

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if(e.getActionCommand() == "RED") {
            getContentPane().setBackground(Color.RED);
        }
        else if(e.getActionCommand() == "YELLOW") {
            getContentPane().setBackground(Color.YELLOW);
        }
        else if(e.getActionCommand() == "GREEN") {
            getContentPane().setBackground(Color.GREEN);
        }
    }

    public static void main(String[] args) {
        new TrafficLight();
    }
}