#Tags
from tkinter import *
def color(event):
    c.itemconfig('group1', width=3,
                 fill="red")
root = Tk()
c = Canvas(width=460, height=150,
           bg='white')
c.pack()
oval = c.create_oval(30, 10, 130, 80, tag="group1")
c.create_line(10, 100, 450, 100, tag="group1")
c.bind('<Button-3>', color)
root.mainloop()