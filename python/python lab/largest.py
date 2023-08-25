#to find the largest of n numbers

n = int(input("Enter the number of numbers: "))

large = 0
for _ in range(n):
    i = int(input("enter the number"))
    if i>large:
        large = i

print(large, "is the largest")