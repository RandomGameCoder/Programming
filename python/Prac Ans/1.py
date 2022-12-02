f=open('MyFile.txt', 'r')
while True:
    line=f.readline()
    if not line:
        break
    for i in line.split():
        print(i,end='#')
    print()
f.close()
