from Tkinter import *


#create a class
class myButtons:
    #Create the constructor that it's going to be call whenever a object of
    #this class is created
    def __init__(self,master): #master = root
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print something",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text="Quit",command=frame.quit) #Exit button with builtin exit function
        self.quitButton.pack(side=RIGHT)                       #frame.quit breaks the mainloop

    def printMessage(self):
        print("This worked!")

#create the main window
root = Tk()
myButtonsObject = myButtons(root) # pass root as a parameter to make it = master
#"run" the main window
root.mainloop()
