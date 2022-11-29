import java.util.Scanner;

class Fib {
    void fib(int a, int b, int n) {
        if (n <= 0) {
            return;
        }
        else if(a+b == 0) {
            if(n>1) {
                System.out.print(a+" ");
                System.out.print(b+1+" ");
                fib(a, b+1, n-2);
            }
            else if(n == 1) {
                System.out.print(a+" ");
            }
            else {
                return;
            }
        }
        else {
            System.out.print(a+b+ " ");
            fib(b, a+b, n-1);
        }
    } 
}

class Fibonacci {
    public static void main(String[] args) {
        int n;
        Scanner read = new Scanner(System.in);
        Fib obj = new Fib();
        System.out.print("Enter the no of terms to be printed: ");
        n = read.nextInt();
        obj.fib(0,0,n);
    }
}