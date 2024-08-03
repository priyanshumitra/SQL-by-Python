#Program to insert the data in table of database
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='Database1')
c=b.cursor()
c.execute("insert into stu(Roll,Name,Course) values(%s,%s,%s)",(21,"Alok Mittal","BBA")) #This library 'execute' also helps to insert the data in table of database but this line can take only data at a time(means, only take it in single row and multiple columns data not more then one row data in database at a time) and this line just helps to take the value and insertion data held by commit() function.
c.execute("insert into stu(Roll,Name,Course) values(%s,%s,%s)",(22,"Dhruv Mittal","BCA"))
b.commit() #It helps to insert the data in table(stu) of database
print("Record Inserted")
