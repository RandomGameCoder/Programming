import random
n=int(input('Enter Number of Digits:'))
l=10**(n-1)
u=10**n-1
r=random.randint(l,u)
print('Number is:',r)
