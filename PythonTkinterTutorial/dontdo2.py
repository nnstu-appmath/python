from tkinter import *

root = Tk()
c = Canvas(width=300, height=300,
           bg='white')
c.focus_set()
c.pack()

ball = c.create_oval(140, 140, 160, 160,
                     fill='green')
c.bind('<Up>',
       lambda event: c.move(ball, 0, -3))
c.bind('<Down>',
       lambda event: c.move(ball, 0, 3))
c.bind('<Left>',
       lambda event: c.move(ball, -3, 0))
c.bind('<Right>',
       lambda event: c.move(ball, 3, 0))

root.mainloop()