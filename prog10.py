#Program to delete all data from table of database
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='database1')
c=b.cursor()
d=('truncate table database1.stu')
c.execute(d)
b.commit()
print("All data Deleted from table(stu) of database")
c.execute("select * from database1.stu") #select all data from database
for c in c.fetchall():  #Print all the data from database by loop after updating 
    print(c)  
    #It will print nothing because all datas are deleted from database
