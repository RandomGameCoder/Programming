import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class Coordinate {
    int x, y;
    Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class SnakeGame extends JFrame implements KeyListener{
    public ArrayList<Coordinate> snake;
    public boolean exit = false;
    public int dir = 4;//N:1, S:2, E:3, W:4
    public int TAIL = 1;

    public SnakeGame() {
        setTitle("~~Snake~~");
        setSize(800,600);
        setResizable(false);
        setLayout(new GridBagLayout());

        setBackground(Color.DARK_GRAY);

        snake = new ArrayList<>();

        snake.add(new Coordinate(110, 100));
        snake.add(new Coordinate(100, 100));

        this.addKeyListener(this);

        repaint();

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
        while(!exit) {
            System.out.println("True");
            Coordinate tail = snake.get(TAIL);
            Coordinate head = snake.get(0);
            snake.remove(TAIL);
            if(dir == 1) {
                tail.y = head.y +10;
            }
            else if(dir == 2) {
                tail.y = head.y -10;
            }
            else if(dir == 3) {
                tail.x = head.x -10;
            }
            else if(dir == 4) {
                tail.x = head.x +10;
            }
            snake.add(0, tail);
            repaint();
            try{
                Thread.sleep(1000);
            }
            catch(InterruptedException e) {
                System.out.println("error");
            }
            
        }
    }

    public void paint(Graphics g) {
        g.clearRect(0, 0, 800, 600);
        g.setColor(Color.WHITE);
        Iterator<Coordinate> it = snake.iterator();
        while(it.hasNext()) {
            Coordinate temp = it.next();
            g.fillRect(temp.x, temp.y, 9, 9);
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {}

    @Override
    public void keyReleased(KeyEvent e) {}

    @Override
    public void keyTyped(KeyEvent e) {}



    public static void main(String[] args) {
        new SnakeGame();
    }
}