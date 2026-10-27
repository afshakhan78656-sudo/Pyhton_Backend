from python_form_db import *
from tkinter import *

root = Tk() #constructor
root.geometry("500x500")
root.title("Registration Form")

id=Label(root,text="Enter ID",font=("Calibri",14,"bold"))
id.place(x=50,y=50)

name=Label(root,text="Enter Name",font=("Calibri",14,"bold"))
name.place(x=50,y=100)

email=Label(root,text="Enter Email",font=("Calibri",14,"bold"))
email.place(x=50,y=150)

mobile=Label(root,text="Enter Mobile",font=("Calibri",14,"bold"))
mobile.place(x=50,y=200)

password=Label(root,text="Enter Password",font=("Calibri",14,"bold"))
password.place(x=50,y=250)

cpassword=Label(root,text="Enter Confirm Password",font=("Calibri",14,"bold"))
cpassword.place(x=50,y=300)

eid=Entry(root,bg="lightgrey")
eid.place(x=280,y=55)

ename=Entry(root,bg="lightgrey")
ename.place(x=280,y=105)

eemail=Entry(root,bg="lightgrey")
eemail.place(x=280,y=155)

emobile=Entry(root,bg="lightgrey")
emobile.place(x=280,y=205)

epassword=Entry(root,bg="lightgrey")
epassword.place(x=280,y=255)

ecpassword=Entry(root,bg="lightgrey")
ecpassword.place(x=280,y=305)

mydb=pymysql.connect(host="localhost",user="root",password="",database="python_form")
mycursor=mydb.cursor()

def insert():
    name=ename.get()
    email=eemail.get()
    mobile=emobile.get()
    password=epassword.get()
    cpassword=ecpassword.get()

    query="insert into form (name,email,mobile,password,cpassword) values ('%s','%s','%s','%s','%s')"
    args=(name,email,mobile,password,cpassword)

    mycursor.execute(query % args)
    mydb.commit()
    print("Data Inserted Successfully!!")

def update():
    id=eid.get()
    name=ename.get()
    email=eemail.get()
    mobile=emobile.get()
    password=epassword.get()
    cpassword=ecpassword.get()

    query="update form set name='%s',email='%s',mobile='%s',password='%s',cpassword='%s' where id='%s'"
    args=(name,email,mobile,password,cpassword,id)

    mycursor.execute(query % args)
    mydb.commit()
    print("Data Updated Successfully!!")

def delete():
    id=eid.get()

    query="delete from form where id='%s'"
    args=(id)

    mycursor.execute(query % args)
    mydb.commit()
    print("Data Deleted Successfully!!")

def search():
    query="select * from form"

    mycursor.execute(query)
    data=mycursor.fetchall()
    print(data)

insert=Button(root,fg="NavyBlue",font=("Calibiri",16,"italic"),text="Insert",command=insert)
insert.place(x=50,y=340)

update=Button(root,fg="NavyBlue",font=("Calibiri",16,"italic"),text="Update",command=update)
update.place(x=140,y=340)

delete=Button(root,fg="NavyBlue",font=("Calibiri",16,"italic"),text="Delete",command=delete)
delete.place(x=250,y=340)

search=Button(root,fg="NavyBlue",font=("Calibiri",16,"italic"),text="Search",command=search)
search.place(x=350,y=340)

root.mainloop()