#Program to connect the Python to MySQL database 

# import mysql.connector (It's very importent to use this library otherwise we can't be able to use mysql by python)
import mysql.connector as hello # We use (mysql.connector) as a veriable(hello) because then it will easy to use
db=hello.connect(host='localhost',user='root',password='Mitra6254@') #we have to write this line in every mysql related program for connect the python to mysql and (db) is an normal veriable that just store this 
print(db,"Hello World") #<mysql.connector.connection.MySQLConnection object at 0x0000013E54BAF750> Hello World(It gives us a surity that programe have no any error)


