#Program to insert multiple data in table(stu) of database at a time 
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='Database1')
c=b.cursor()
d=("insert into stu(Roll,Name,Course) values(%s,%s,%s)") #This line make the structure of Columns and we must give the value as column order otherwise it will give error. This line stored in normal variable (d).
e=[(27,"Rohan Jurel",'BCA'),(29,"Om Kaar","BBA"),(34,"Mohan Gupta","PGDM"),
    (41,"Harsh Panchal","MBA"),(27,"Rohan Jurel",'BCA')]   #I just make the list for collect multiple datas at a time we can use tuple also for collect multiple data.
c.executemany(d,e) # 'executemany' library is also under in cursor() function it's use for take the multiple data at a time and their parameter order represent 'd' stands by structure of data query and 'e' stands by data
b.commit() #It helps to insert the data in table of database
print("Record Inserted")