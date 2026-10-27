import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists python_form")
mydb.commit()


mydb=pymysql.connect(host="localhost",user="root",password="",database="python_form")
mycursor=mydb.cursor()

mycursor.execute("create table if not exists form(id int primary key auto_increment,name varchar(50),email varchar(50),mobile bigint,password varchar(50),cpassword varchar(50))")
mydb.commit()