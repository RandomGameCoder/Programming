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
    public int dir = 3;//N:1, S:2, E:3, W:4
    public int TAIL = 2;
    public Random cherryGenerator;
    public Coordinate cherry;

    public SnakeGame() {
        setTitle("~~Snake~~");
        setSize(800,600);
        setResizable(false);
        setLayout(new GridBagLayout());

        setBackground(Color.DARK_GRAY);

        snake = new ArrayList<>();
        cherryGenerator = new Random();

        snake.add(new Coordinate(110, 100));
        snake.add(new Coordinate(100, 100));
        snake.add(new Coordinate(90, 100));

        cherry = new Coordinate(cherryGenerator.nextInt(0, 20), cherryGenerator.nextInt(600));

        this.addKeyListener(this);

        repaint();

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
        while(!exit) {
            Coordinate tail = snake.get(TAIL);
            Coordinate head = snake.get(0);
            snake.remove(TAIL);
            if(dir == 1) {
                if(head.y == 0) {
                    tail.y = 590;
                }
                else {
                    tail.y = head.y -10;
                }
                tail.x = head.x;
            }
            else if(dir == 2) {
                if(head.y == 590) {
                    tail.y = 0;
                }
                else {
                    tail.y = head.y +10;
                }
                tail.x = head.x;
            }
            else if(dir == 3) {
                if(head.x == 0) {
                    tail.x = 790;
                }
                else {
                    tail.x = head.x -10;
                }
                tail.y = head.y;
            }
            else if(dir == 4) {
                if(head.x == 790) {
                    tail.x = 0;
                }
                else {
                    tail.x = head.x +10;
                }
                tail.y = head.y;
            }
            snake.add(0, tail);
            repaint();
            try{
                Thread.sleep(300);
            }
            catch(InterruptedException e) {
                System.out.println("error");
            }
            
        }
    }

    public void paint(Graphics g) {
        g.clearRect(0, 0, 800, 600);
        g.setColor(Color.RED);
        g.fillOval(cherry.x, cherry.y, 9, 9);
        g.setColor(Color.WHITE);
        Iterator<Coordinate> it = snake.iterator();
        while(it.hasNext()) {
            Coordinate temp = it.next();
            g.fillRect(temp.x, temp.y, 9, 9);
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if(e.getKeyCode() == e.VK_W) {
            dir = 1;
        }
        else if(e.getKeyCode() == e.VK_S) {
            dir = 2;
        }
        else if(e.getKeyCode() == e.VK_A) {
            dir = 3;
        }
        else if(e.getKeyCode() == e.VK_D) {
            dir = 4;
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {}

    @Override
    public void keyTyped(KeyEvent e) {}



    public static void main(String[] args) {
        new SnakeGame();
    }
}