
def stats (filename):
    longest = ''
    for line in filename.readlines():
        if len(line) > len(longest):
            longest = line
    print("Longest Line's Length is", len(longest))
    print(longest)

fh = open("try.txt",'r')
stats(fh)
fh.close()
