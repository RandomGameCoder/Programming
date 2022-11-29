import java.util.Scanner;

class Prime {
    public static void main(String[] args) {
        int n, f = 0,i = 2;
        Scanner read = new Scanner(System.in);
        System.out.print("Enter a number: ");
        n = read.nextInt();
        while(i<(n/i)) {
            if(n%i == 0) {
                System.out.println("The given number is not a prime number.");
                f = 1;
                break;
            }
            i++;
        }
        if(f == 0) {
            System.out.println("The given number is a prime number.");
        }
    }
}