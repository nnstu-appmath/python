from tkinter import *
from tkinter import ttk
def operation():

    a = int(e1.get())
    b = int(e2.get())
    if bottom["text"] =="+":
        leftdata = str(a + b)
    if bottom["text"]=="-":
        leftdata = str(a - b)
        print("hi")
    if bottom["text"]=="*":
        leftdata = str(a * b)
    if bottom["text"]=="/":
        leftdata = str(a / b)

    left["text"]=""
    left.insert(1, leftdata)
def selection():
    selection = "You selected the option " + str(radio.get())
    label.config(text=selection)

operationname="+"
def choseaddition():
    bottom.config(text="+")
def chosesubtraction():
    bottom.config(text="-")
def chosemultiplication():
    bottom.config(text="*")
def chosedivision():
    bottom.config(text="/")

root=Tk()
root.geometry("400x250")
file = Menu(root)
file.add_command(label="+",command=choseaddition)
file.add_command(label="-",command=chosesubtraction)
file.add_command(label="*",command=chosemultiplication)
file.add_command(label="/",command=chosedivision)
root.config(menu=file)
w1 = PanedWindow(root)
w1.pack( )
left = Entry(w1, bd=5)
w1.add(left)
w2 = PanedWindow(w1, orient=VERTICAL)
w1.add(w2)
e1 = Entry(w2)
e2 = Entry(w2)
w2.add(e1)
w2.add(e2)
bottom = Button(w2,text="+", command=operation)
w2.add(bottom)

radio = IntVar()
mainloop()