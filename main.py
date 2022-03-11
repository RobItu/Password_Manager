from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) <= 0 or len(password) <= 0 or len(email_username) <= 0:
        messagebox.showwarning(title="ERROR", message="Please make sure all entries are filled")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=190)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_password_button = Button(text="Generate Password", command=gen_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

window.mainloop()
