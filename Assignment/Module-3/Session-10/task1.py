from tkinter import *

root = Tk()
root.title("My Playlist")
root.geometry("400x300")

label = Label(root, text="Welcome to Your Music Playlist",
              font=("Arial", 14))
label.place(x=40, y=50)

root.mainloop()