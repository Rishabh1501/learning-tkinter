from tkinter import *

root = Tk()
#create a label widget
my_label = Label(root,text="Hello World!")
#pushing onto the screen (very-unsophisticated way)
my_label.pack()

#calling the main loop
root.mainloop()
