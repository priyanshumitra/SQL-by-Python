#Program to delete the data from table of database
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='database1')
c=b.cursor()
d=("delete from database1.stu where name=%s and course=%s") #This line for delete the data
e=("Alok Mittal","BBA") #Compare that data in table of database when it will match then their related data will be delete from table of database
c.execute(d,e) #It take that data
b.commit() #It will insert that data for comparision in table of database which will be delete
print(c.rowcount,"Data Deleted") # 'c.rowcount' show the how many data deleted by rows 
c.execute("select * from database1.stu") #select all data from table(stu) of database
for c in c.fetchall():  #Print all the data from table of database by loop after updating 
    print(c)