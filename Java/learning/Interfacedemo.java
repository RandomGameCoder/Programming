import java.util.Scanner;
interface Shape{
    public void number_of_sides();
    //public double area();
}
interface Area extends Shape{
    public double area();

}

class Rectangle implements Area{
    double l,b;
    Rectangle(double l,double b){
        this.l=l;
        this.b=b;
    }
    public void number_of_sides(){
        System.out.println("4 sides");
    }
    public double area(){
        return l*b;
    }
}

class Triangle implements Area{
    double a,b,c;
    Triangle(double a,double b,double c){
        this.a=a;
        this.b=b;
        this.c=c;
    }
    public void number_of_sides(){
        System.out.println("3 sides");
    }
    public double area(){
        double s=(a+b+c)/2;
        return Math.sqrt(s*(s-a)*(s-b)*(s-c));
    }
}

class Hexagon implements Area{
    double s;
    Hexagon(double s){
        this.s=s;
    }
    public void number_of_sides(){
        System.out.println("6 sides");
    }
    public double area(){
        double r=1.732;
        return(3*r*s*s)/2;
    }
}

class Interfacedemo{
    public static void main(String[] args){
        double a,b,c;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the length of rectangle:");
        a=sc.nextInt();
        System.out.println("Enter the breadth of rectangle:");
        b=sc.nextInt();
        Area obj1=new Rectangle(a, b);
        obj1.number_of_sides();
        System.out.println("Area of rectangle is:"+obj1.area());

        System.out.println("\nEnter the side a of triangle:");
        a=sc.nextInt();
        System.out.println("Enter the side b of triangle:");
        b=sc.nextInt();
        System.out.println("Enter the side c of triangle:");
        c=sc.nextInt();
        Area obj2=new Triangle(a, b,c);
        obj2.number_of_sides();
        System.out.println("Area of rectangle is:"+obj2.area());

        System.out.println("\nEnter the side of hexagon:");
        a=sc.nextInt();
        Area obj3=new Hexagon(a);
        obj3.number_of_sides();
        System.out.println("Area of rectangle is:"+obj3.area());
    }
}