n = int(input("Enter a number:"))
end = n
i = 2
while i<=end:
    print(i,end)
    if n%i == 0:
        print("number is not prime")
        end = 0
        break
    end = n//i
    i+=1
if end !=0:
    print("number is prime")