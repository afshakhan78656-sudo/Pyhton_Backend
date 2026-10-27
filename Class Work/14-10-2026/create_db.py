import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycurser=mydb.cursor()

mycurser.execute("create database if not exists python400")
mydb.commit()



mydb = pymysql.connect(host="localhost",user="root",password="", database="python400")
mycurser=mydb.cursor()

mycurser.execute("create table if not exists python100(id int primary key auto_increment,name varchar(50),mobile bigint)")
mydb.commit()
