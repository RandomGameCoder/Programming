import java.util.Scanner;

class Transpose {
	public static void main(String[] args) {
		int m, n;
		Scanner read = new Scanner(System.in);
		System.out.print("Enter the dimensions of the matrix: ");
		m = read.nextInt();
		n = read.nextInt();
		int a[][] = new int[m][n];
		int b[][] = new int[n][m];
		System.out.println("Enter the matrix elements: ");
		for(int i = 0; i<m; i++) {
			for(int j = 0; j<n; j++) {
				a[i][j] = read.nextInt();
				b[j][i] = a[i][j];
			}
		}
		System.out.println("The transpose of the given matrix is: ");
		for(int i = 0; i<m; i++) {
			for(int j = 0; j<n; j++) {
				System.out.print(b[j][i]+ " ");
			}
			System.out.println();
		}
	}
}