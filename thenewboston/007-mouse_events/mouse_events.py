from Tkinter import *

#create the main window
root = Tk()

def leftClick(event):
    print("left")
def rightClick(event):
    print("Right")
def middleClick(event):
    print("Middle")

frame = Frame(root,width = 600,height = 400) #adjust the size of the window
#bind multiple functions to different mouse events
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)

#pack the frame to the main window
frame.pack()
#"run" the main window
root.mainloop()
