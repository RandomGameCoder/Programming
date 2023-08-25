#show percentage of students

name = input("Enter the name: ")
rollno = int(input("enter Roll no: "))
total = int(input("Enter total marks for subject: "))
s1 = int(input("enter marks for subject1: "))
s2 = int(input("enter marks for subject2: "))
s3 = int(input("enter marks for subject3: "))

per = ((s1+s2+s3)/(total*3))*100
print("Total marks: ", s1+s2+s3, ", percentage: ", per)

if per>=50:
    print("pass")
    if per >= 90:
        print("Excellent.")
    elif per < 90 and per >= 80:
        print("Good.")
    elif per < 80 and per >= 70:
        print("Satisfactory.")
    else:
        print("Poor.")
else:
    print("fail")