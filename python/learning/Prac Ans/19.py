import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',passwd='root')
mycur=con.cursor()
mycur.execute('use school')
mycur.execute('select * from student')
print('Given records are:')
for x in mycur:
    print(x)
rn=int(input('Enter the roll no of student for name update:'))
nm=input("Enter the name:")
qry="update student set name=%s where rn=%s"
val=(nm,rn)
mycur.execute(qry,val)
print('Name updated')
mycur.execute('select * from student')
for x in mycur:
    print(x)
con.commit()
con.close()
