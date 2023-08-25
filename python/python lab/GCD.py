#to find the GCD of two numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(min(a,b), 0, -1):
    if a%i == 0 and b%i == 0:
        print("The GCD is", i)
        break