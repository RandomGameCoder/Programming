def remove_lowercase(first, second):
    opf = open(second, "w")
    inf = open(first, "r")
    for line in inf:
        if line[0].islower():
            pass
        else:
            opf.write(line)

remove_lowercase('a.txt', 'b.txt')
fh = open("b.txt", 'r')
print(fh.read())
