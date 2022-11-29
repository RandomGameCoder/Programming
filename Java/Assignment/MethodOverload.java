import java.util.Scanner;
import java.lang.Math;

class Shape {
    double area(double l, double b) {
        return l*b;
    }
    double area(double a, double b, double c) {
        double s = (a+b+c)/2;
        return Math.sqrt(s*(s-a)*(s-b)*(s-c));
    }
    double area(double r) {
        return 3.1415*r*r;
    }
}

class MethodOverload {
    public static void main(String[] args) {
        double a, b, c, area;
        Shape obj = new Shape();
        Scanner read = new Scanner(System.in);
        System.out.print("Enter the radius of the circle: ");
        a = read.nextDouble();
        area = obj.area(a);
        System.out.println("The area of the circle is "+area);
        System.out.print("Enter the dimensions of the rectangle: ");
        a = read.nextDouble();
        b = read.nextDouble();
        area = obj.area(a,b);
        System.out.println("The area of the rectangle is "+area);
        System.out.print("Enter the sides of the triangle: ");
        a = read.nextDouble();
        b = read.nextDouble();
        c = read.nextDouble();
        area = obj.area(a,b,c);
        System.out.println("The area of the triangle is "+area);
    }
}