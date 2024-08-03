#Program to fetch the data related to company and do other operations with their database(company)
import mysql.connector as db
a=db.connect(host='localhost',user='root',password='Mitra6254@',database='company')
b=a.cursor()
list1=[]
wish=input("You want to insert the data in database(Yes/No): ")
if(wish=='Yes'):
          e=("insert into emp(ID,Name,Job) values(%s,%s,%s)")
          n=int(input("Enter the Total Number of Employes: "))
          for i in range(n):
    
                            ID=int(input("Enter the Employe ID: "))
                            name=input("Enter the Name of Employe: ")
                            job=input("Enter the Job of Employe: ")
                            group=(ID,name,job)
                            list1.append(group)
          b.executemany(e,list1)
          a.commit()
          print("Your all Data inserted in the Database successfully")
          print("Here is Your New Database :=")
          b.execute("select * from company.emp") 
          for b in b.fetchall():  
                   print(b)
elif(wish=="No"):
        print("Here is Your Previous Database :=")
        b.execute("select * from company.emp") 
        for b in b.fetchall():  
            print(b)

else:
        print("You Entered Wrong Value please choose betwwen(Yes/No)")
        wish=input("You want to insert the data in database(Yes/No): ")
        if(wish!='Yes' or 'No'):
                
           while(wish!='Yes' or 'No'):
                print("You Entered Wrong Value please choose betwwen(Yes/No)")
                wish=input("You want to insert the data in database(Yes/No): ")
                if(wish=='Yes'):
                    e=("insert into emp(ID,Name,Job) values(%s,%s,%s)")
                    n=int(input("Enter the Total Number of Employes: "))
                    for i in range(n):
                
                                        ID=int(input("Enter the Employe ID: "))
                                        name=input("Enter the Name of Employe: ")
                                        job=input("Enter the Job of Employe: ")
                                        group=(ID,name,job)
                                        list1.append(group)
                    b.executemany(e,list1)
                    a.commit()
                    print("Your all Data inserted in the Database successfully")
                    print("Here is Your New Database :=")
                    b.execute("select * from company.emp") 
                    for b in b.fetchall():  
                            print(b)
                    exit(0)
                elif(wish=="No"):
                        print("Here is Your Previous Database :=")
                        b.execute("select * from company.emp") 
                        for b in b.fetchall():  
                            print(b)
                        exit(0)
                






