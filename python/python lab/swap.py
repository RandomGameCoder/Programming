#swap two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("the numbers before swapping: ", a,b)
a,b = b,a
print("the numbers after swapping: ", a,b)