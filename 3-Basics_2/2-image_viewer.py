import os
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#adding a title
root.title("Image-Viewer")

#adding a favicon/icon
root.iconbitmap("3-Basics_2\\favicon.ico")

# #adding an image
# my_img = ImageTk.PhotoImage(Image.open("3-Basics_2\\images\\picture.png"))
# #creating a label for the image
# my_label = Label(root, image=my_img)
# my_label.grid(row=0, column=0, columnspan=3)

#scanning the image folder and putting it in list

#list the directories inside image folder
images = os.listdir("3-Basics_2\\images")
image_list = [i for i in images]

#variable for position in relative to image_list
position = 0


#function for buttons
def forward():
    global my_label
    global my_img
    global image_list
    global position

    my_label.grid_forget()
    if position == len(image_list) - 1:
        position = 0
    else:
        position = position + 1

    my_img = ImageTk.PhotoImage(
        Image.open("3-Basics_2\\images\\" + image_list[position]))
    my_label = Label(root, image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)


def backword():
    global my_label
    global my_img
    global image_list
    global position

    my_label.grid_forget()

    if position == 0:
        position = len(image_list) - 1
    else:
        position = position - 1

    my_img = ImageTk.PhotoImage(
        Image.open("3-Basics_2\\images\\" + image_list[position]))
    my_label = Label(root, image=my_img)
    my_label.grid(row=0, column=0, columnspan=3)
    
    
def refresh():
    global my_img
    global image_list
    
    images = os.listdir("3-Basics_2\\images")
    image_list = [i for i in images]


#adding an image
my_img = ImageTk.PhotoImage(
    Image.open("3-Basics_2\\images\\" + image_list[position]))
#creating a label for the image
my_label = Label(root, image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

#creating the buttons
forward_button = Button(root,
                        text=">>",
                        fg="#2E86C1",
                        bg="#2C3E50",
                        command=forward)
back_button = Button(root,
                     text="<<",
                     fg="#2E86C1",
                     bg="#2C3E50",
                     command=backword)

refresh_button = Button(root,
                        text="Refresh Images",
                        fg="#2E86C1",
                        bg="#2C3E50",
                        command=refresh)

#grid-ing the buttons
forward_button.grid(row=1, column=2)
back_button.grid(row=1, column=0)
refresh_button.grid(row = 1, column= 1)

#running the main loop
root.mainloop()
