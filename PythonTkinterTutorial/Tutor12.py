from tkinter import *
def selection():
    selection = "You selected the option " + str(radio.get())
    label.config(text=selection)

top = Tk()
top.geometry("600x450")
radio = IntVar()
lbl = Label(text="Favourite programming language:")
lbl.pack()
R1 = Radiobutton(top, text="C", variable=radio, value=1,
                 command=selection)
R1.pack(anchor=W)
R2 = Radiobutton(top, text="C++", variable=radio, value=2,
                 command=selection)
R2.pack(anchor=W)
R3 = Radiobutton(top, text="Java", variable=radio, value=3,
                 command=selection)
R3.pack(anchor=W)
label = Label(top)
label.pack()
spin = Spinbox(top, from_= 0, to = 25)
spin.pack()
top.mainloop()