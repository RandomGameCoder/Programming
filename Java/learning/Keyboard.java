import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Keyboard extends JFrame {
    public JLabel display;
    public JButton[] buttons;
    public Keyboard() {
        setTitle("Keyboard");
        setSize(700,200);
        setLayout(new FlowLayout());
        buttons = new JButton[48];
        String keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,,./";
        for(int i = 0; i<48; i++) {
            buttons[i] = new JButton(String.valueOf(keys.charAt(i)));
            add(buttons[i]);
        }
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new Keyboard();
    }
}