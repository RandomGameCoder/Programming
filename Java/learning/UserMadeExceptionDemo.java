import java.util.*;
import java.io.*;

class NewSampleException extends Exception {
    public NewSampleException(String s) {
        super(s);
    }
}

public class UserMadeExceptionDemo {
    public static void main(String[] args) throws NewSampleException {
        Scanner read = new Scanner(System.in);
        int a = read.nextInt();
        if(a == 0) {
            throw new NewSampleException("0 input given");
        }
        else {
            System.out.println("Good to go");
        }
    }
}