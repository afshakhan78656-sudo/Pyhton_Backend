from tkinter import *

root = Tk()
root.title("Music Actions")
root.geometry("350x200")

b1 = Button(root, text="Like")
b1.place(x=50, y=40)

b2 = Button(root, text="Share")
b2.place(x=180, y=40)

b3 = Button(root, text="Download")
b3.place(x=50, y=100)

b4 = Button(root, text="Add to Queue")
b4.place(x=180, y=100)

root.mainloop()