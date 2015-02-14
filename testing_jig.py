from tkinter import *

def donothing():
    print('fucker')

def menu(root):
    topMenu = Menu(root)

    fileMenu = Menu(topMenu, tearoff=0)
    fileMenu.add_command(label="New", command=donothing)
    fileMenu.add_command(label="Open", command=donothing)
    fileMenu.add_command(label="Save", command=donothing)
    fileMenu.add_command(label="Save as...", command=donothing)
    fileMenu.add_command(label="Close", command=donothing)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=root.quit)
    topMenu.add_cascade(label="File", menu=fileMenu)

    functionMenu = Menu(topMenu, tearoff=0)
    functionMenu.add_command(label="Undo", command=donothing)
    functionMenu.add_separator()
    functionMenu.add_command(label="Cut", command=donothing)
    functionMenu.add_command(label="Copy", command=donothing)
    functionMenu.add_command(label="Paste", command=donothing)
    functionMenu.add_command(label="Delete", command=donothing)
    functionMenu.add_command(label="Select All", command=donothing)
    topMenu.add_cascade(label="Function", menu=functionMenu)

    graphMenu = Menu(topMenu, tearoff=0)
    graphMenu.add_command(label="Graph", command=donothing)
    topMenu.add_cascade(label="Graph", menu=graphMenu)

    helpMenu = Menu(topMenu, tearoff=0)
    helpMenu.add_command(label="Help Index", command=donothing)
    helpMenu.add_command(label="About...", command=donothing)
    topMenu.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=topMenu)
    root.mainloop()

root = Tk()
menu(root)
