from tkinter import *
from menu_setup import *
from menu_functions import *

root = Tk()
Label(root, text="First").grid(row=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
b1 = Button(root, text="test", command=printMe(e1))
b1.grid(row=0, column=2)

menu(root)