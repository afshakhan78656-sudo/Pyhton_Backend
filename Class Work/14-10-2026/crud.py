from create_db import *

mydb=pymysql.connect(host="localhost",user="root",passwd="",database="python400")
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
    choice=int(input("Enter the Choice:"))

    if choice==1:
        name=input("Enter Name:")
        mobile=int(input("Enter Mobile:"))

        query="insert into python100(name,mobile) values ('%s','%s')"
        args=(name,mobile)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Inserted!!")

    elif choice==2:
        id=int(input("Enter ID:"))
        name=input("Enter Name:")
        mobile=int(input("Enter Mobile:"))

        query="update python100 set name='%s',mobile='%s' where id='%s' "
        args=(name,mobile,id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Updated!!")

    elif choice==3:
        id=int(input("Enter ID:"))

        query="delete from python100 where id='%s'"
        args=(id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted!!")


    elif choice==4:
        query="select * from python100"

        mycurser.execute(query)
        data=mycurser.fetchall()
        print(data)

    elif choice==5:
        print("Exit!!")

    else:
        print("Invalid Choice!!")