#to find the sum of the squares of the first n natural numbers

n = int(input("Enter a number: "))

sum = 0
for i in range(1,n+1):
    sum += i**2
print("the sum of first",n,"natural numbers squares is", sum)