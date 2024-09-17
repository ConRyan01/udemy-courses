from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as f:
        f.write('Website | Email | Password\n')

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        message = messagebox.showerror(title='Oops!', message='Please fill out each entry field')
        return None

    isokay = messagebox.askyesno(title=website, message=f'These are the details entered: \n{website}\n{username}\n{password}\nIs this correct?')

    if isokay:
        f = open("data.txt", "a")
        f.write(f'{website} | {username} | {password}\n')
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        f.close()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, padx=50, pady=50)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_password_btn = Button(text='Generate Password', command=generate_password)
gen_password_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=34, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
