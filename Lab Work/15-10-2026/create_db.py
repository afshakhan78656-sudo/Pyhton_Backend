import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists college")
mydb.commit()


mydb=pymysql.connect(host="localhost",user="root",password="",database="college")
mycursor=mydb.cursor()

mycursor.execute("create table if not exists student(id int primary key auto_increment,name varchar(50),mobile bigint,age int,address varchar(50))")
mydb.commit()