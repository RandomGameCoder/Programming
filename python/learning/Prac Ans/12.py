n=int(input('Enter First Number:'))
m=int(input('Enter Second Number:'))
n1=n%10
m1=m%10
print(n1, m1)
if n1<m1:
    print('The Number is:',n)
else:
    print('The Number is:',m)
