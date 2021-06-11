from tkinter import *

root = Tk()

#you can combine various attributes together to make an amazing button
#creating a button
button = Button(root, text='Enabled')
button.pack()

#creating a disabled button
disabled_button = Button(root, text='Disabled', state='disabled')
disabled_button.pack()

#creating a x padded button
x_padded_button = Button(root, text='x-padded', padx=50)
x_padded_button.pack()

#creating a y padded button
y_padded_button = Button(root, text='y-padded', pady=50)
y_padded_button.pack()


#action/function for a button
def myclick():
    label = Label(root, text='You Clicked a Button!')
    label.pack()

action_button = Button(root, text='Action-Button', command=myclick)
action_button.pack()

#changing foreground color of a button
fg_button = Button(root, text='fg-colored-button', fg= 'cyan')
fg_button.pack()

#changing background color of a button
bg_button = Button(root, text='bg-colored-button', bg= 'red')
bg_button.pack()

#calling the main loop
root.mainloop()
