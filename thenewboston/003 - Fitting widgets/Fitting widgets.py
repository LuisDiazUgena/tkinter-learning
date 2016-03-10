from Tkinter import *

#create the main window
root = Tk()

one = Label(root,text="One",bg="red",fg="white")
one.pack()
two = Label(root,text="Two",bg="green",fg="black")
two.pack(fill=X)
three = Label(root,text="Three",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)
#"run" the main window
root.mainloop()
