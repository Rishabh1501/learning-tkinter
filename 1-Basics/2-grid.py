from tkinter import *

root = Tk()
#create a label widget
my_label1 = Label(root, text="Hello World!")
my_label2 = Label(root, text="My name is Rishabh")

#using grid instead of pack()
my_label1.grid(row=0, column=1)
my_label2.grid(row=1, column=1)

#calling the main loop
root.mainloop()
