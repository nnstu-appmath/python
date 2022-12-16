from tkinter import *
from tkinter import ttk
def get_value():
   e_text=entry.get()
   Label(win, text=e_text, font= ('Century 15 bold')).pack(pady=20)

win= Tk()
win.geometry("750x250")
#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)
#Create a button to display the text of entry widget
button= ttk.Button(win, text="Enter", command= get_value)
button.pack()

win.mainloop()