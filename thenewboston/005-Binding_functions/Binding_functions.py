from Tkinter import *

#create the main window
root = Tk()

#Technique 1
#create the functions
def printName():
    print("Hello, my name is Inigo Montoya")

#bind the button to a function
button = Button(root,text="Print my name",command = printName).pack()

#Technique 1
#create the functions
def printQuote(event):
    print("You killed my father, prepare to die")

button2 = Button(root,text="Print quoute")
#left mouse click event = <Button-1>
button2.bind("<Button-1>",printQuote)
button2.pack()
#"run" the main window
root.mainloop()
