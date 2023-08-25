#to check whether the given number is a palindrome or not

n = int(input("Enter a number: "))

n1, n2 = n, 0
while n1!=0:
    lsb = n1%10
    n1 //= 10
    n2 = n2*10+lsb

if n2 == n:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")