#to print n fibonacci numbers

n = int(input("Enter a number"))

a, b = 0, 1
for i in range(0,n):
    print(a, end = " ")
    b = a+b
    a = b-a