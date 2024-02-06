from tkinter import *

def rect_func(event):
    c.delete("rect")
    c.create_text(230, 50,
                  text="Прямоугольник")

c = Canvas(width=460, height=100,
           bg='grey80')
c.pack()
c.create_rectangle(180, 10, 280, 80,
                   tag="rect",
                   fill="lightgreen")
trian = c.create_polygon(
    330, 80, 380, 10, 430, 80,
    fill='white', outline="black",tag="rect")
c.tag_bind("rect", '<Button-1>', rect_func)

mainloop()