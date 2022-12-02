import csv
# To create a CSV File by writing individual lines
def CreateCSV1():
    # Open CSV File
    Csvfile = open('student1.csv', 'w', newline='')
    # CSV Object for writing
    Csvobj = csv.writer(Csvfile)
    while True:
        Rno = int(input("Rno:"))
        Name = input("Name:")
        Marks = float(input("Marks:"))
        Line = [Rno, Name, Marks]
        # Writing a line in CSV file
        Csvobj.writerow(Line)
        Ch = input("Enter More Records(Y/N)?")
        if Ch.lower() == 'n':
            break
    Csvfile.close() # Closing a CSV File

# To create a CSV File by writing all lines in one go
def CreateCSV2():
    # Open CSV File
    Csvfile = open('student1.csv', 'w', newline='')
    # CSV Object for writing
    Csvobj =csv.writer(Csvfile)
    Lines = []
    while True:
        Rno = int(input("Rno:"))
        Name = input("Name:")
        Marks = float(input("Marks:"))
        Lines.append([Rno, Name, Marks])
        Ch = input("Enter More Records(Y/N)?")
        if Ch.lower() == 'n':
            break
    # Writing all lines in CSV file
    Csvobj.writerows(Lines)
    Csvfile.close() # Closing a CSV File

# To read and show the content of a CSV File
def ShowAll():
    # Opening CSV File for reading
    Csvfile = open('student1.csv', 'r', newline='')
    # Reading the CSV content in object
    Csvobj = csv.reader(Csvfile)
    for Line in Csvobj: # Extracting line by line content
        print(Line)
    Csvfile.close() # Closing a CSV File

print("CSV File Handling")
while True:
    Option = input("1:CreateCSV 2:CreateCSVAll 3:ShowCSV 4:Quit :")
    if Option == "1":
        CreateCSV1()
    elif Option == "2":
        CreateCSV2()
    elif Option == "3":
        ShowAll()
    elif Option == "4":
        break
    else:
        print("Invalid Choice!!")
