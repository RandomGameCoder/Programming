import java.util.Scanner;

class StrRev {
    public static void main(String args[]) {
        String str,rev = "";
        Scanner read = new Scanner(System.in);
        System.out.print("Enter a string: ");
        str = read.nextLine();
        for(int i = str.length()-1; i>=0; i--) {
            rev = rev + str.charAt(i);
        }
        System.out.print("The reversed string is: " +rev);
    }
}