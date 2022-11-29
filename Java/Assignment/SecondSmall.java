import java.util.Scanner;

class SecondSmall {
    public static void main(String[] args) {
        int n, min, temp;
        Scanner read = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        n = read.nextInt();
        int a[] = new int[n];
        System.out.print("Enter array elements: ");
        for(int i = 0; i<n; i++) {
            a[i] = read.nextInt();
        }
        for(int i = 0; i<2; i++) {
            min = i;
            for(int j = i+1; j<n; j++) {
                if(a[j]<a[min]) {
                    min = j;
                }
            }
            if(min!=i) {
                temp = a[min];
                a[min] = a[i];
                a[i] = temp;
            }
        }
        System.out.println("The second smallest element in the array is " +a[1]);
    }
}