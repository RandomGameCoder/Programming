import java.io.*; // for handling input/output
import java.util.*; // contains Collections framework

// don't change the name of this class
// you can add inner classes if needed
class Main {
    public static void main (String[] args) {
        int T,N,L;
        long S,sum;
        Scanner read = new Scanner(System.in);
        T = read.nextInt();
        for(int i = 0; i<T; i++) {
            N = read.nextInt();
            L = read.nextInt();
            S = read.nextLong();
            if(L == N-1) {
                sum = (long) (N*(N+1))/2;
                if(S-sum >0 && S-sum <=N) {
                    System.out.println("YES");
                }
                else {
                    System.out.println("NO");
                }
            }
            else {
                System.out.println("NO");
            }
        }
    }
}