#Animations
from random import *

from tkinter import *

def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] <300:
        root.after(10, motion)
def recolor(event):
    color="#"
    for i in range(6):
        ranc1=choice("ABCDEF1234567890")
        color+=ranc1
    c.itemconfig(ball,
                 fill=color)

root = Tk()
c = Canvas(root, width=600, height=200,
           bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140,
                     fill='green')
c.tag_bind(ball, '<Button-1>', recolor)
motion()
root.mainloop()