from tkinter import *
from tkinter.ttk import *
master = Tk()
master.geometry("200x200")
# function to open a new window
# on a button click
def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text="This is a new window").pack()

label = Label(master,
              text="This is the main window")
label.pack(pady=10)
# a button widget which will open a new window on button click
btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)
mainloop()