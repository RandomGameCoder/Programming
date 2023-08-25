#find the largest of three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a>b and a>c:
    print(a,"is the largest")
elif b>c:
    print(b,"is the largest")
else:
    print(c,"is the largest")