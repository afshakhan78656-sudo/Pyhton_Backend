from tkinter import *

def login():
    username = e1.get()
    password = e2.get()

    if username != "" and password != "":
        result.config(text="Login Successful")
    else:
        result.config(text="Please fill all fields")

root = Tk()
root.title("Login Form")
root.geometry("400x300")

l1 = Label(root, text="Username")
l1.place(x=50, y=50)

e1 = Entry(root)
e1.place(x=150, y=50)

l2 = Label(root, text="Password")
l2.place(x=50, y=100)

e2 = Entry(root, show="*")
e2.place(x=150, y=100)

b1 = Button(root, text="Login", command=login)
b1.place(x=150, y=150)

result = Label(root, text="")
result.place(x=120, y=200)

root.mainloop()