import java.util.Random;

class EvenPrint extends Thread {
    int num;
    EvenPrint(int num) {
        this.num = num;
    }
    public void run() {
        for(int i = 2; i<=num; i+=2) {
            System.out.println(i);
        }
    }
}

class OddPrint extends Thread {
    int num;
    OddPrint(int num) {
        this.num = num;
    }
    public void run() {
        for(int i = 1; i<=num; i+=2) {
            System.out.println(i);
        }
    }
}

class RandomThread extends Thread {
    public void run() {
        int ri;
        EvenPrint ep;
        OddPrint op;
        Random r = new Random();
        for(int i = 0; i<10; i++) {
            ri = r.nextInt(100);
            System.out.println("The Random Number is " +ri);
            if(ri%2 == 0) {
                ep = new EvenPrint(ri);
                ep.start();
            }
            else {
                op = new OddPrint(ri);
                op.start();
            }
            try{
                Thread.sleep(1000);
            } catch(InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class MultiThreadDemo {
    public static void main(String[] args) {
        RandomThread r = new RandomThread();
        r.start();
    }
}
