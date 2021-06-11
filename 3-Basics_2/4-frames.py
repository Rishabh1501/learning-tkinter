from tkinter import *

root = Tk()
#creating a title
root.title("Frames")
#adding an icon
root.iconbitmap("3-Basics_2\\favicon.ico")

#creating the frame
frame = LabelFrame(root, text="Welcome to Frame", padx=10, pady=10)
frame.pack(padx=10, pady=10)

#creating a button inside the frame
button = Button(frame, text="Inside Frame")
button.pack()

#running the mainloop
root.mainloop()