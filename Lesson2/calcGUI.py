# T R Hoshino
# 13/09/2022

# ***************************************************
# Python Calculator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library 

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
        
    except SyntaxError:

        equation_text.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

# Design the user interface

window = Tk()
window.title("Python Calculator")
window.geometry("500x500")
window.configure(bg="#c9f5ed")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, width=9, height=4, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, width=9, height=4, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, width=9, height=4, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, width=9, height=4, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, width=9, height=4, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, width=9, height=4, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, width=9, height=4, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, width=9, height=4, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, width=9, height=4, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, width=9, height=4, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# create operation button

plus = Button(frame, text='+', width=9, height=4, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=4)

minus = Button(frame, text='-', width=9, height=4, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=4)

multiply = Button(frame, text='x', width=9, height=4, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=4)

divide = Button(frame, text='/', width=9, height=4, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=4)

# create equals button

equal = Button(frame, text='=', width=9, height=4, font=35, command=equals)
equal.grid(row=3, column=2)

# create decimal button
decimal = Button(frame, text='.', width=9, height=4, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

# create clear button
clear = Button(window, text='clear', width=12, height=4, font=35, command=clear)
clear.pack()

window.mainloop()