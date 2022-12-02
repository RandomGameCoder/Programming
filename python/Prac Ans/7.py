#  A text file contains Alphanumeric text. Write a Python code to read that file and prints only the numbers/ digits of that file.
fh = open("alnum.txt")
for line in fh:
    words = line.split()
    for i in words:
        for letter in i:
            if letter.isdigit():
                print(letter)
