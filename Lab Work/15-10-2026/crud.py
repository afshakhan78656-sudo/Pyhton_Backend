from create_db import *

mydb=pymysql.connect(host="localhost",user="root",password="",database="college")
mycursor=mydb.cursor()

while True:
    menu="""
    press 1 for Insert Data
    press 2 for Update Data
    press 3 for Delete Data
    press 4 for Fetch Data
    press 5 for Exit
"""
    print(menu)
    choice=int(input("Enter Choice:"))

    if choice==1:
        name=input("Enter Name:")
        mobile=int(input("Enter Mobile:"))
        age=int(input("Enter Age:"))
        address=input("Enter Address:")

        query="insert into student(name,mobile,age,address)values('%s','%s','%s','%s')"
        args=(name,mobile,age,address)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Inserted!!")

    elif choice==2:
        id=int(input("Enter ID:"))
        name=input("Enter Name:")
        mobile=int(input("Enter Mobile:"))
        age=int(input("Enter Age:"))
        address=input("Enter Address:")

        query="update student set name='%s',mobile='%s',age='%s',address='%s' where id='%s'"
        args=(name,mobile,age,address,id)

        mycursor.execute(query %args)
        mydb.commit()
        print("Data Updated!!")

    elif choice==3:
        id=int(input("Enter ID:"))

        query="delete from student where id='%s'"
        args=(id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted!!")

    elif choice==4:
        query="select * from student"

        mycursor.execute(query) 
        data=mycursor.fetchall() #
        print(data)
        print("Data Fetch!!")

    elif choice==5:
        print("Thank uh!!")

    else:
        print("Invalid Chice!!")