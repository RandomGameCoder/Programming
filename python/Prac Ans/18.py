import mysql.connector
con = mysql.connector.connect(host='localhost',user='root',passwd='root')
mycur=con.cursor()
mycur.execute('use school')
mycur.execute('select * from student')
print('Given records are:')
for x in mycur:
    print(x)
mycur.execute("insert into student values(12, 'Geeta', 10)")
mycur.execute('select * from student')
print('Records after insertion are:')
for x in mycur:
    print(x)
con.close()
