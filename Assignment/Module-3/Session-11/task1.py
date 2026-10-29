import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

print("Connection successful")

mydb.close()