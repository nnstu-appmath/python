from tkinter import *
root = Tk()
c = Canvas(root, width=600, height=600, bg='white')
c.pack()
c.create_line(10, 10, 190, 50)
c.create_line(100, 180, 100, 60, fill='green',
              width=5, arrow=LAST, dash=(10, 2),
              activefill='lightgreen',
              arrowshape="10 20 10")
c.create_rectangle(110, 110, 290, 160)
c.create_rectangle(160, 180, 240, 290,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

root.mainloop()