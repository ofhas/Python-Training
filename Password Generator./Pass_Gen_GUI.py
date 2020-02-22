from tkinter import *
import tkinter.messagebox
import random
from tkinter.ttk import Combobox
import pyperclip

root = Tk()
root.geometry("500x500")
root.title("Password Generator")

var = IntVar()
var1 = IntVar()


def exit1():
    exit()

def pass_generator():
    entry.delete(0, END) # in order to delete the previous password that was generated in case the output isn't desirable

    length = var1.get()
    digits_only = "0123456789"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_and_small = "ABCDEFGpqrIJKHdefstuvwxyzQRSTUghijklmnoLMNOPabcVWXYZ"
    upper_small_numbers = "ABCDEF567STUst38auvJKjkVwxyz012bcdeflQR49"
    all_types = "JKLM45678NOPQR3ST29~!fghiUVWX)_+|}{CYZabmnopqAB(DEFGHIrstuvwxyz01jkl@#$%^&*[]'/.,`"

    new_length = int(length)

    if var.get() == 1:
        password = random.choices(digits_only, k=new_length)
        return "".join(password)

    if var.get() == 2:
        password = random.choices(small_letters, k=new_length)
        return "".join(password)

    if var.get() == 3:
        password = random.choices(upper_letters, k=new_length)
        return "".join(password)

    if var.get() == 4:
        password = random.choices(upper_and_small, k=new_length)
        return "".join(password)

    if var.get() == 5:
        password = random.choices(upper_small_numbers, k=new_length)
        return "".join(password)

    if var.get() == 6:
        password = random.choices(all_types, k=new_length)
        return "".join(password)


def generate():
    new_pass = pass_generator()
    entry.insert(10, new_pass)


def copy1():
    copy_pass = entry.get()
    pyperclip.copy(copy_pass)


def instructions():
    tkinter.messagebox.showinfo("Types of passwords on the scale:", "1: Digits\n2: Small letters\n3: Upper letters\n4: Upper & small letters\n"
    "5: Upper & small letters & digits\n6: All characters ")


label1 = Label(root, text = "Choose password type:")
label1.place(x=50, y=75)

label2 = Label(root, text = "Weak to strong:")
label2.place(x=185, y=40)

Random_password = Label(root, text="Password:")
Random_password.place(x=105, y=200)
entry = Entry(root)
entry.place(x=175, y=200)

generate_button = Button(root, text="Generate",width = 12, bg="green", fg="white", command=generate)
generate_button.place(x=190 , y=160)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.place(x = 305, y=197)

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
