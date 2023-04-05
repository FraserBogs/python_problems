"""
Exporting the Project

Project name : "Calculator with Tkinter"
Date and Time : 3/30/2023 22:52:43

University : BSU - Baku State University
Faculty : Applied Mathematics and Cybernetics (SABAH Groups)
Majority : Computer Sciences
Course : Two (2)
Group name : KE022S1 and KE022S2
Students : Sultanova Gulchohra Cavanshir and Aliyev Zakir Agamehdi

Note : If there is any problem with the issue, please contact
aliyevzakir814@gmail.com or gulcohrsultanov@gmail.com :)
"""

from tkinter import *


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


# Create the GUI
root = Tk()
root.title("Calculator")
root.config(bg="dark blue")
root.geometry("410x770")

e = Entry(root, width=24, borderwidth=10, font=("Arial", 20))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, bg="blue", text="1", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(1))
button_2 = Button(root, bg="blue", text="2", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(2))
button_3 = Button(root, bg="blue", text="3", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(3))
button_4 = Button(root, bg="blue", text="4", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(4))
button_5 = Button(root, bg="blue", text="5", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(5))
button_6 = Button(root, bg="blue", text="6", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(6))
button_7 = Button(root, bg="red", text="7", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(7))
button_8 = Button(root, bg="red", text="8", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(8))
button_9 = Button(root, bg="red", text="9", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(9))
button_0 = Button(root, bg="red", text="0", padx=41, pady=20, font=("Arial", 30), command=lambda: button_click(0))

button_add = Button(root, font=("Arial", 30), bg="green", text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, font=("Arial", 30), bg="green", text="-", padx=45, pady=20, command=button_subtract)
button_multiply = Button(root, font=("Arial", 30), bg="green", text="*", padx=45, pady=20, command=button_multiply)
button_divide = Button(root, font=("Arial", 30), bg="green", text="/", padx=46, pady=20, command=button_divide)
button_equal = Button(root, font=("Arial", 30), bg="green", text="=", padx=110, pady=20, command=button_equal)
button_clear = Button(root, font=("Arial", 30), bg="red", text="Clear", padx=75, pady=20, command=button_clear)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()