#Program to create Database
import mysql.connector as X
hello=X.connect(host='localhost',user='root',password='Mitra6254@')
a=hello.cursor() # cursor() function has multiple of oprations related to database 
a.execute("create database database1") # 'execute' library is also under in cursor() function and this program line create the database with the help of execute library and "create database" is not just a string it also work as a keyword to make database and database name should be not have any space between their database name otherwise it will throw error.
#We should write all commands,databases name, tables name and more related to MySQL in small letters because if you'll try to write they in capital letters then it will automatically form in small letters.
print("Database Created")
