#Program to print all databases in MySQL and Tables in their databases
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='Database1')
c=b.cursor()
c.execute('create table Emp(ID int,Name varchar(50),Department varchar(20))') #Createing another table(emp) in database
print("Here is Our all Databases are present in MySQL:-")
print(" ")
c.execute("Show Databases") #This library 'execute' also helps to show the databases
for i in c:
    print(i)
print(" ")
print("Here is Our all Tables are present in database1:-")
print(" ")
c.execute("Show Tables") #This library 'execute' also helps to show the tables
for i in c:
    print(i)
