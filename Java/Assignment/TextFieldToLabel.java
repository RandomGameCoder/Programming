import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class TextFieldToLabel extends JFrame implements ActionListener{
    private JTextField textfield1;
    private JTextField textfield2;
    private JLabel label;
    private JButton button;
    private String str1, str2;

    public TextFieldToLabel() {
        setTitle("Text Field to Label");
        setSize(250, 170);
        setLayout(new FlowLayout());
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        textfield1 = new JTextField(20);
        textfield2 = new JTextField(20);
        label = new JLabel("label");
        button = new JButton("Click here");

        label.setPreferredSize(new Dimension(200, 30));

        add(textfield1);
        add(textfield2);
        add(label);
        add(button);

        button.addActionListener(this);

        setVisible(true);
    }

    public void actionPerformed(ActionEvent ae) {
        str1 = textfield1.getText();
        str2 = textfield2.getText();
        label.setText(str1 +"  "+ str2);
    }
    
    public static void main(String[] args) {
        new TextFieldToLabel();
    }
}