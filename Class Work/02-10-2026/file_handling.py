# file=open("task1.txt","w")
# file.write("Write Here!!")
# file.close()

# file=open("task1.txt","a")
# file.write("\nAppend Here!!")
# file.close()

# file=open("task1.txt","r")
# print(file.read())
# file.close()

# l=[]

# for i in range(1,11):
#     l.append(i)

# file=open("task2.txt","w")
# file.write(str(l))
# file.close()


#write and read both (w+)
# file=open("task3.txt","w+")
# file.write("w+ is here!!")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

#write and read both (r+)   existing file hi read karega

file=open("task3.txt","r+")
print(file.tell())
file.seek(0)
print(file.read())
file.close()
