#to show armstrong numbers within the given number

n = int(input("Enter the number: "))

for i in range(1,n+1):
    l = 0
    n1, n2 = i, 0
    while n1!=0:
        lsb = n1%10
        n1 //= 10
        n2 = n2*10+lsb50
        l += 1

    n1, n2 = i, 0
    while n1!=0:
        lsb = n1%10
        n1 //= 10
        n2 += lsb**l

    if n2 == i:
        print(i, end=" ")