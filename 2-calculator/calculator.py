from tkinter import *

root = Tk()
root.title("Simple Calculator")

#entry widget/ imput for our calculator
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, padx=10, pady=10, columnspan=3
       )  #columnspan is for centering it with columns/ buttons beneath

numbers = []
operations = []

def insert(number):
    e.insert(END,number)


def clear():
    e.delete(0,END)
    numbers.clear()
    operations.clear()

def addition():
    numbers.append(int(e.get()))
    operations.append('+')
    e.delete(0,END)

def multiply():
    numbers.append(int(e.get()))
    operations.append('*')
    e.delete(0,END)

def divide():
    numbers.append(int(e.get()))
    operations.append('/')
    e.delete(0,END)

def subtract():
    numbers.append(int(e.get()))
    operations.append('-')
    e.delete(0,END)

def equals():
    numbers.append(int(e.get()))
    e.delete(0,END)
    print(numbers)
    print(operations)
    for i in range(0,len(operations)):    
        print('i = ',i)
        if i==0:
            s = numbers[i]
            if operations[i] == '+':
                s = s + numbers[i+1] 
            elif operations[i] == '*':
                s = s * numbers[i+1]
            elif operations[i] == '-':
                s = s - numbers[i+1]
            elif operations[i] == '/':
                s = s / numbers[i+1]
        else:
            if operations[i] == '+':
                s = s + numbers[i+1] 
            elif operations[i] == '*':
                s = s * numbers[i+1]
            elif operations[i] == '-':
                s = s - numbers[i+1]
            elif operations[i] == '/':
                s = s / numbers[i+1]  
        
    e.insert(0,s)
    numbers.clear()
    operations.clear()


#defining buttons
button_1 = Button(root, text='1', command=lambda: insert(1), padx=40, pady=25)
button_2 = Button(root, text='2', command=lambda: insert(2), padx=40, pady=25)
button_3 = Button(root, text='3', command=lambda: insert(3), padx=40, pady=25)

button_4 = Button(root, text='4', command=lambda: insert(4), padx=40, pady=25)
button_5 = Button(root, text='5', command=lambda: insert(5), padx=40, pady=25)
button_6 = Button(root, text='6', command=lambda: insert(6), padx=40, pady=25)

button_7 = Button(root, text='7', command=lambda: insert(7), padx=40, pady=25)
button_8 = Button(root, text='8', command=lambda: insert(8), padx=40, pady=25)
button_9 = Button(root, text='9', command=lambda: insert(9), padx=40, pady=25)

button_0 = Button(root, text='0', command=lambda: insert(0), padx=40, pady=25)
button_clear = Button(root, text='Clear', command=clear, padx=79, pady=25)
button_add = Button(root, text='+', command=addition, padx=40, pady=25)
button_equals = Button(root, text='=', command=equals, padx=89, pady=25)
button_multiply = Button(root, text='*', command=multiply, padx=40, pady=25)
button_divide = Button(root, text='/', command=divide, padx=40, pady=25)
button_subtract = Button(root, text='-', command=subtract, padx=40, pady=25)

#grid-ing of buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equals.grid(row=6, column=1, columnspan=2)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=6, column=0)
button_subtract.grid(row=5, column=2)

#running the mainloop
root.mainloop()