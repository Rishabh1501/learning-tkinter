from tkinter import *
from PIL import ImageTk, Image


root = Tk()
#adding a title
root.title("Images")

#adding a favicon/icon
root.iconbitmap("3-Basics_2\\favicon.ico")

#adding an image
my_img = ImageTk.PhotoImage(Image.open("3-Basics_2\\picture.png"))
#creating a label for the image
my_label = Label(root,image=my_img)
my_label.pack()


#running the main loop
root.mainloop()