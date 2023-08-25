#find roots of a quadratic equation
import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

t = b*b-4*a*c

if t<0:
    print("the roots are imaginary")
else:
    r1 = (-b + math.sqrt(t))/(2*a)
    r2 = (-b - math.sqrt(t))/(2*a)
    print("the roots are",r1,"and",r2)