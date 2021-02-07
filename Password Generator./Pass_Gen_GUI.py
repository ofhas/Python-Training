#!/usr/bin/env python3
from tkinter import *
import tkinter.messagebox
import random
import pyperclip

root = Tk()
root.geometry("500x500")
root.title("Password Generator")

var = IntVar()
var1 = IntVar()


def exit1():
    exit()


def digits(length):
    digitsString = []
    for i in range(48, 58):
        digitsString.append(chr(i))
    digitsString = random.choices(digitsString, k=length)
    return "".join(digitsString)


def smallLetters(length):
    smallLetterString = []
    for i in range(97, 123):
        smallLetterString.append(chr(i))
    smallLetterString = random.choices(smallLetterString, k=length)
    return "".join(smallLetterString)


def upperCaseLetters(length):
    upperCaseString = []
    for i in range(65, 91):
        upperCaseString.append(chr(i))
    upperCaseString = random.choices(upperCaseString, k=length)
    return "".join(upperCaseString)


def upperAndLowerCase(length):
    upperAndLower = []
    for i in range(97, 123):
        upperAndLower.append(chr(i))
    for i in range(65, 91):
        upperAndLower.append(chr(i))
    upperAndLower = random.choices(upperAndLower, k=length)
    return "".join(upperAndLower)


def upperLowerNumbers(length):
    upperLowerAndNumbers = []
    for i in range(97, 123):
        upperLowerAndNumbers.append(chr(i))
    for i in range(65, 91):
        upperLowerAndNumbers.append(chr(i))
    for i in range(48, 58):
        upperLowerAndNumbers.append(chr(i))
    upperLowerAndNumbers = random.choices(upperLowerAndNumbers, k=length)
    return "".join(upperLowerAndNumbers)


def allChars(length):
    allCharString = []
    for i in range(33, 127):
        allCharString.append(chr(i))
    allCharString = random.choices(allCharString, k=length)
    return "".join(allCharString)


def pass_generator():
    entry.delete(0,
                 END)  # in order to delete the previous password that was generated in case the output isn't desirable

    length = var1.get()

    new_length = int(length)

    if var.get() == 1:
        password = digits(new_length)
        return "".join(password)

    if var.get() == 2:
        password = smallLetters(new_length)
        return "".join(password)

    if var.get() == 3:
        password = upperCaseLetters(new_length)
        return "".join(password)

    if var.get() == 4:
        password = upperAndLowerCase(new_length)
        return "".join(password)

    if var.get() == 5:
        password = upperLowerNumbers(new_length)
        return "".join(password)

    if var.get() == 6:
        password = allChars(new_length)
        return "".join(password)


def generate():
    new_pass = pass_generator()
    entry.insert(10, new_pass)


def copy1():
    copy_pass = entry.get()
    pyperclip.copy(copy_pass)


def instructions():
    tkinter.messagebox.showinfo("Types of passwords on the scale:",
                                "1: Digits\n2: Small letters\n3: Upper letters\n4: Upper & small letters\n"
                                "5: Upper & small letters & digits\n6: All characters ")


label1 = Label(root, text="Choose password type:")
label1.place(x=50, y=75)

label2 = Label(root, text="Weak to strong:")
label2.place(x=185, y=40)

Random_password = Label(root, text="Password:")
Random_password.place(x=105, y=200)
entry = Entry(root)
entry.place(x=175, y=200)

generate_button = Button(root, text="Generate", width=12, bg="green", fg="white", command=generate)
generate_button.place(x=190, y=160)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.place(x=305, y=197)

label3 = Label(root, text="Length of password:")
label3.place(x=50, y=120)

password_type = Scale(root, from_=1, to=6, orient=HORIZONTAL, variable=var)
password_type.place(x=190, y=60)

password_length = Scale(root, from_=8, to=50, orient=HORIZONTAL, variable=var1)
password_length.place(x=190, y=100)
quit_button = Button(root, text="Quit", width=12, bg="red", fg="white", command=exit1).place(x=190, y=260)

menu = Menu(root)

root.config(menu=menu)

menu.add_command(label="Instructions", command=instructions)

root.mainloop()
