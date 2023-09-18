from tkinter import *
import random
import string
import pyperclip

def generate_password():
    length = int(length_box.get())
    complexity = choice.get()

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        pass_field.delete(0, END)
        pass_field.insert(0, "Invalid complexity level")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    pass_field.delete(0, END)
    pass_field.insert(0, password)

def copy():
    cp = pass_field.get()
    pyperclip.copy(cp)


root = Tk()
root.title("🔐 Password Generator")
root.geometry("400x400")
root.config(bg="lightblue")

choice = IntVar()
font = ('Arial', 13, 'bold')


title_label = Label(root, text="Password Generator", font=("Arial", 20, 'bold'), bg='lightblue', fg='purple')
title_label.pack(pady=5)


emoji_label = Label(root, text="🔐", font=("Arial", 40), bg='lightblue', fg='purple')
emoji_label.pack()


weak_radio_bt = Radiobutton(root, text='Weak', value=1, variable=choice, font=font, bg='lightblue', fg='purple')
weak_radio_bt.pack(pady=5)

med_radio_bt = Radiobutton(root, text='Medium', value=2, variable=choice, font=font, bg='lightblue', fg='purple')
med_radio_bt.pack(pady=5)

strong_radio_bt = Radiobutton(root, text='Strong', value=3, variable=choice, font=font, bg='lightblue', fg='purple')
strong_radio_bt.pack(pady=5)


length_label = Label(root, text="Password Length", font=font, bg='lightblue', fg='purple')
length_label.pack(pady=5)

length_box = Spinbox(root, from_=4, to=20, width=5, font=font)
length_box.pack(pady=5)


gen_bt = Button(root, text="Generate Password", font=font, bg='purple', fg='white', command=generate_password)
gen_bt.pack(pady=5)


pass_field = Entry(root, width=25, bd=2, font=font)
pass_field.pack(pady=5)

copy_bt = Button(root, text="Copy", font=font, bg='purple', fg='white', command=copy)
copy_bt.pack(pady=5)

root.mainloop()
