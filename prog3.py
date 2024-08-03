#Program to create the Table in Database1
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='Database1') #We must be declare that database in that line which we will working on it
c=b.cursor()
c.execute('create table stu(Roll int,Name varchar(50),Course varchar(20))') #This library 'execute' also helps to create the table
print('Table Created')