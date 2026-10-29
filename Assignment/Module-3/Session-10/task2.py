from tkinter import *

def play():
    result.config(text="Playing")

def pause():
    result.config(text="Paused")

def next_song():
    result.config(text="Next Song")

root = Tk()
root.title("My Playlist")
root.geometry("400x300")

label = Label(root, text="My Music Playlist")
label.place(x=130, y=20)

b1 = Button(root, text="Play", command=play)
b1.place(x=50, y=80)

b2 = Button(root, text="Pause", command=pause)
b2.place(x=150, y=80)

b3 = Button(root, text="Next", command=next_song)
b3.place(x=250, y=80)

result = Label(root, text="Select an action")
result.place(x=140, y=140)

root.mainloop()