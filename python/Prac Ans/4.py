import pickle

f1 = open('a.dat','wb')
print("Enter the students' detail:")
n = eval(input('How many details you want to enter: '))
detail = {}
for i in range(n):
    print('\nEnter Details for Student ',i+1)
    rn = eval(input('Enter Roll No: '))
    nm = input('Name  of Student: ')
    mr= eval(input('Enter total marks out of 500:'))
    detail[rn] = [nm,mr]

pickle.dump(detail,f1)
f1.close()

f1 = open('a.dat','rb')
d=pickle.load(f1)
t=eval(input('Enter Roll no to be updated:'))
if t in d.keys():
    print('Name is ',d[t][0], 'and marks are', d[t][1])
    m=eval(input('Enter New Marks:'))
    d[t][1]=m
    print('Updated Details are:')
    print('Name is ',d[t][0], 'and marks are', d[t][1])
else:
    print("Roll no doesn't exist")
