from Tkinter import *
import tkMessageBox

mainwindow = Tk()
#Callback
def info():
   tkMessageBox.showinfo( "(Pi)2 Commander", "Hello World")

def slider():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

#Widgets go here

#4,5,6,21,22,27,25,28,29

button0 = Button(mainwindow, text ="GPIO-0", command = info)
button2 = Button(mainwindow, text ="GPIO-2", command = info)
button3 = Button(mainwindow, text ="GPIO-3", command = info)
button4 = Button(mainwindow, text ="GPIO-4", command = info)
button5 = Button(mainwindow, text ="GPIO-5", command = info)
button6 = Button(mainwindow, text ="GPIO-6", command = info)
button21 = Button(mainwindow, text ="GPIO-21", command = info)
button22 = Button(mainwindow, text ="GPIO-22", command = info)
button25 = Button(mainwindow, text ="GPIO-25", command = info)
button27 = Button(mainwindow, text ="GPIO-27", command = info)
button28 = Button(mainwindow, text ="GPIO-28", command = info)
button29 = Button(mainwindow, text ="GPIO-29", command = info)
#pack buttons
button0.pack(anchor=W)
button2.pack(anchor=W)
button3.pack(anchor=W)
button4.pack(anchor=W)
button5.pack(anchor=W)
button6.pack(anchor=W)
button21.pack(anchor=W)
button22.pack(anchor=W)
button25.pack(anchor=W)
button27.pack(anchor=W)
button28.pack(anchor=W)
button29.pack(anchor=W)

#PWM 1, 23,26,24,
pwm1 = DoubleVar()
pwm23 = DoubleVar()
pwm24 = DoubleVar()
pwm26 = DoubleVar()

pwm1 = Scale(mainwindow,variable=pwm1)
#pack pwm
pwm1.pack(anchor=E)

#Run the mainloop (mainwindow)
mainwindow.mainloop()
