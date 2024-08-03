#Program to update the data of table of database and print it also
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='database1')
c=b.cursor()
d=('update database1.stu set roll=%s where name=%s and course=%s ') #This line is for update the data of table of database(in this line ham 'set' ke baad jiss bhi chiz ko update karna cahte hain bas ussko vahan likhdo after that 'where' is compare the data in database for matching the datarow which has to been update)
e=(101,"Alok Mittal",'BBA') #Updating data
c.execute(d,e) #It take the data 
b.commit() #That is insert the updated data in table(stu) of database and replace old value and place new value which is updated
print("Database Updated")
c.execute("select * from database1.stu") #select all data from table(stu) of database
for c in c.fetchall():  #Print all the data from table of database by loop after updating 
    print(c)
