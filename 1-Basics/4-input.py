from tkinter import *

root = Tk()

#entry widget for inputing
e = Entry(root)
e.pack()
e.insert(0, "Enter Your Name:")  #Inputs default text inside the entry widget/ input bar

#some parameter for entry widget
# to change width => width= <value>
# to change height => height= <value>
# to change color fg and bg

#changing borderwidth
# borderwidth = Entry(root, borderwidth=10)
# borderwidth.pack()


#working input and button fields
def entry_func():
    text = e.get()  #for getting the value from the entry widget
    label = Label(root,
                  text=f'Hello! {text}')  #label for displaying the input value
    label.pack()


button = Button(root, text="Enter Your Name", command=entry_func)
button.pack()

#running the mainloop
root.mainloop()