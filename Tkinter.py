#tkinter 

from tkinter import *

root = Tk() # creat new window
root.title("name of window") # namgozari panjere 
root.geometry("250x200") # tain andaze default 
root.resizable(width = False , height = False)

name = StringVar() # variable gabel khandan dar tkinter 
def fun():
    name.set('my name is Reza')


bt = Button(root,text = "show name", command = lambda: fun()) # sakht button 
bt.place(x = 10 , y = 10 ) # tain makan bt 

label = Label(root , textvariable = name) # sakh label baraye namayesh string
label.place(x = 50 , y = 50) # makan label 






root.mainloop()


