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
    public String scoreboard;
    public int score;

    public SnakeGame() {
        setTitle("~~Snake~~");
        setSize(800,600);
        setResizable(false);
        setLayout(new GridBagLayout());

        setBackground(Color.DARK_GRAY);

        snake = new ArrayList<>();
        cherryGenerator = new Random();
        score = 0;
        scoreboard = Integer.toString(score);

        snake.add(new Coordinate(110, 100));
        snake.add(new Coordinate(100, 100));
        snake.add(new Coordinate(90, 100));

        cherry = new Coordinate(cherryGenerator.nextInt(1, 78)*10, cherryGenerator.nextInt(4, 55)*10);

        this.addKeyListener(this);

        repaint();

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
        while(!exit) {
            Coordinate tail = new Coordinate(0, 0);
            Coordinate head = snake.get(0);
            if(CherryEaten()) {
                score++;
                scoreboard = Integer.toString(score);
                TAIL++;
            }
            else {
                snake.remove(TAIL);
            }
            if(dir == 1) {
                if(head.y == 50) {
                    tail.y = 580;
                }
                else {
                    tail.y = head.y -10;
                }
                tail.x = head.x;
            }
            else if(dir == 2) {
                if(head.y == 580) {
                    tail.y = 50;
                }
                else {
                    tail.y = head.y +10;
                }
                tail.x = head.x;
            }
            else if(dir == 3) {
                if(head.x == 10) {
                    tail.x = 780;
                }
                else {
                    tail.x = head.x -10;
                }
                tail.y = head.y;
            }
            else if(dir == 4) {
                if(head.x == 780) {
                    tail.x = 10;
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

    public boolean CherryEaten() {
        Coordinate head = snake.get(0);
        if(head.x == cherry.x && head.y == cherry.y) {
            cherry = new Coordinate(cherryGenerator.nextInt(1, 78)*10, cherryGenerator.nextInt(4, 55)*10);
            return true;
        }
        return false;
    }

    public void paint(Graphics g) {
        g.clearRect(0, 0, 800, 600);
        g.setColor(Color.RED);
        g.drawRect(10, 50, 780, 550);
        g.fillOval(cherry.x, cherry.y, 9, 9);
        g.setColor(Color.WHITE);
        g.drawString(scoreboard, 15, 48);
        Iterator<Coordinate> it = snake.iterator();
        while(it.hasNext()) {
            Coordinate temp = it.next();
            g.fillRect(temp.x, temp.y, 9, 9);
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        if(e.getKeyCode() == KeyEvent.VK_W && dir != 2) {
            dir = 1;
        }
        else if(e.getKeyCode() == KeyEvent.VK_S && dir != 1) {
            dir = 2;
        }
        else if(e.getKeyCode() == KeyEvent.VK_A && dir != 4) {
            dir = 3;
        }
        else if(e.getKeyCode() == KeyEvent.VK_D && dir != 3) {
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