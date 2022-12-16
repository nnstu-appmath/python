from tkinter import *


def oval_func(event):
    c.delete(oval)
    c.create_text(80, 50,
                  text="Круг")

def rect_func(event):
    c.delete("rect")
    c.create_text(230, 50,
                  text="Прямоугольник")

def triangle(event):
    c.delete(trian)
    c.create_text(380, 50,
                  text="Треугольник")

c = Canvas(width=460, height=100,
           bg='grey80')
c.pack()
oval = c.create_oval(30, 10, 130, 80,
                     fill="orange")
c.create_rectangle(180, 10, 280, 80,
                   tag="rect",
                   fill="lightgreen")
trian = c.create_polygon(
    330, 80, 380, 10, 430, 80,
    fill='white', outline="black")
c.tag_bind(oval, '<Button-1>', oval_func)
c.tag_bind("rect", '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)

mainloop()