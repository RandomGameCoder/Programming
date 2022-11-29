money = int(input())
if money>181 or money<1:
    print("not possible")
else:
    l = [1,2,5,10]
    c = [0,0,0,0]
    f = []
    for i in l:
        c = [0,0,0,0]
        if money % i == 0:
            c[l.index(i)] = money//i
            print(c[0],c[1],c[2],c[3])
    c = [0,0,0,0]
    m = money
    i = 2
    while m!=0 and i<money:
        while m%i == 0:
            f.append(i)
            m=m//i
        print(i)
        i+=1
    print(f)
    