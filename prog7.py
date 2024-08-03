#Program to print all the data from table of database
import mysql.connector as a
b=a.connect(host='localhost',user='root',password='Mitra6254@',database='Database1')
c=b.cursor()
c.execute("select * from database1.stu") #This library 'execute' also helps to show the data from table of database and (*) means all and this line actually work as take all the data from table of database 
for c in c.fetchall(): #this fetchall() function help to print the all data from table(stu) of database in console(We should be use the loop when we want to print the data in console because it will print the data as straight forward). If you want to print only one data from table of database in console then use fetchone() function by place off fetchall() function
    print(c) #Print the data one by one 
