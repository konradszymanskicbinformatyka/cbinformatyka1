from tkinter import *
import tkinter.messagebox


window = tkinter.Tk()
var = StringVar()
C1Var = tkinter.IntVar()

C1 = tkinter.Radiobutton(window,text='Black', variable=C1Var,value=1)
C2 = tkinter.Radiobutton(window,text='White', variable=C1Var,value=2)
C3 = tkinter.Radiobutton(window,text='Yellow', variable=C1Var,value=3)

label = Label(window, textvariable=var, relief=RAISED, bg='yellow', fg='red')
label.pack()
var.set("Sup!? Whats your race?")

C1.pack()
C2.pack()
C3.pack()


def click():
    print(lb1.selection_get())


lb1 = Listbox(window)
lb1.insert(0,'C')
lb1.insert(1,'C++')
lb1.insert(2,'C#')
lb1.insert(3,'PHP')
lb1.insert(4,'Javascript')
lb1.pack()


B = tkinter.Button(window, text='Submit', command=click)
B.pack()


window.mainloop()
