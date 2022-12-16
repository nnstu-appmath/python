from tkinter import *
top = Tk()
top.geometry("200x250")
menubutton = Menubutton(top, text="Language")
menubutton.grid()
menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu
menubutton.menu.add_checkbutton(label="Russian")
menubutton.menu.add_checkbutton(label="English")
menubutton.pack()
top.mainloop()