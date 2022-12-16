from tkinter import *
from tkinter import ttk
master = Tk()
master.geometry("400x400")

nname="иван"
ppassword="дубков"

def get_value():
   e_text1=entry1.get()
   e_text2=entry2.get()
   if(e_text1==nname)and(e_text2==ppassword):
       openNewWindow()
   else:
       sayurwrong()

def sayurwrong():
    falselabel=Label(master,
          text="password incorrect")
    falselabel.grid(row = 6, column = 1)

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    # A Label widget to show in toplevel
    Label(newWindow,
          text="password correct").pack()

name = Label(master,text = "Name").grid(row = 0, column = 0)
entry1= ttk.Entry(master)
entry1.grid(row = 0, column = 1)
password = Label(master,text = "Password").grid(row = 1, column = 0)
entry2= ttk.Entry(master)
entry2.grid(row = 1, column = 1)

submit = Button(master, text = "Submit", command= get_value).grid(row = 4, column = 0)

label = Label(master,text="Введите пароль").grid(row = 5, column = 0)

mainloop()
