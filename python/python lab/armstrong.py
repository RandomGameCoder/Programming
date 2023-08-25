#to check whether the given number is an armstrong number or not

n = int(input("Enter the number: "))

l = 0
n1, n2 = n, 0
while n1!=0:
    lsb = n1%10
    n1 //= 10
    n2 = n2*10+lsb
    l += 1

n1, n2 = n, 0
while n1!=0:
    lsb = n1%10
    n1 //= 10
    n2 += lsb**l
    

if n2 == n:
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")