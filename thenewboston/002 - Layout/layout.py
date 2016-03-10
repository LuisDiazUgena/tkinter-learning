from Tkinter import *

#create the main window
root = Tk()

#Frame (layout container)
topFrame = Frame(root)
topFrame.pack(side=TOP) #not need to pass TOP parameter
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label = Label(bottomFrame,text="Hello world!",fg = "red")
label.pack(side=RIGHT)
#create buttons

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")
#and now pack the buttons

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

#"run" the main window
root.mainloop()
