from Tkinter import *

#create the main window
root = Tk()

#create widgets
label_user = Label(root,text = "User")
label_pass = Label(root,text= "Password")

entry_user = Entry(root)
entry_pass = Entry(root)

checkbox = Checkbutton(root,text = "Keep me logged in")

#put everything in a grid layout
label_user.grid(row = 0,sticky = E)
label_pass.grid(row = 1,sticky = E)

entry_user.grid(row= 0, column = 1,sticky = W)
entry_pass.grid(row= 1, column = 1,sticky = W)

checkbox.grid(columnspan = 2,sticky = E) # Merge it in two columns
#"run" the main window
root.mainloop()
