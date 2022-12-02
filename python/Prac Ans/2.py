v=c=u=l=0
f=open('MyFile.txt','r')
d=f.read()
f.close()
for i in d:
    for j in i.split():
        for k in j:
            if k.lower() in ('a','e','i','o','u'):
                v+=1
            else:
                c+=1
            if k.islower():
                l+=1
            else:
                u+=1
print('Total Vowels are:',v)
print('Total Consonents are:',c)
print('Total lowercase chars are:',l)
print('Total uppercase chars are:',u)
