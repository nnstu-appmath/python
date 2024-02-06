from tkinter import *
parent1 = Tk()
parent1.geometry("200x100")
def printer(event):
    print("Hello World!")
redbutton = Button(parent1, text= "Red", fg = "red")
redbutton.pack( side = LEFT)
greenbutton = Button(parent1, text = "Green", fg = "green")
greenbutton.pack( side = RIGHT )
bluebutton = Button(parent1, text = "Blue", fg = "blue")
bluebutton.pack( side = TOP )
blackbutton = Button(parent1, text = "Black", fg = "black")
blackbutton.pack( side = BOTTOM)

blackbutton.bind("<Button-1>", printer)
bluebutton.bind("<Button-3>", printer)

parent1.mainloop()