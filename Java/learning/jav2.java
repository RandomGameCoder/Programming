import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class jav2 extends JFrame
{
  private JLabel label;
  private JTextField text1;
  private JTextField text2;
  private JButton button;

  public jav2()
  {
    setLayout(new FlowLayout());

    text1 = new JTextField(10);
    add(text1);

    text2 = new JTextField(10);
    add(text2);

    button = new JButton("Submit");
    add(button);

    event e = new event();
    button.addActionListener(e);
    
    label = new JLabel("Enter Values:");
    add(label);
  }

  public class event implements ActionListener
  {
    public void actionPerformed(ActionEvent e)
    {
      String val1 = text1.getText();
      String val2 = text2.getText();
      label.setText("Value 1: " + val1);
      label.setText("Value 2: " + val2);
    }
  }

  public static void main(String[] args)
  {
    jav2 form = new jav2();
    form.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    form.setSize(500, 500);
    form.setVisible(true);
  }
}
