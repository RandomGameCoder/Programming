import pickle

f1 = open('a.dat','wb')
print("Enter the students' detail:")
n = eval(input('How many details you want to enter: '))
detail = {}
for i in range(n):
    print('\nEnter Details for Student ',i+1)
    rn = eval(input('Enter Roll No: '))
    nm = input('Name  of Student: ')
    detail[rn] = nm

pickle.dump(detail,f1)
f1.close()
f1 = open('a.dat','rb')
test = pickle.load(f1)
print(test)

sh = eval(input('\nEnter Roll No of Student You are Looking For: '))
if sh in test.keys():
    print('Name is:', test[sh])
else:
    print('Not Found')
