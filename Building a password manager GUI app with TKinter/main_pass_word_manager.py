from tkinter import *
from tkinter import messagebox as mbox
from random import randint, shuffle, choice #In order not to use random."something" use it to use only "something"
import pyperclip
import json

from watchdog.watchmedo import command

# ---------------------------- SEARCH DATA -------------------------------------- #

def search():
    website = website_entry.get()

    try:
        with open("passwords.json", "r") as data_file:
            data_dict = json.load(data_file)

            email = data_dict[website]["email"]
            password = data_dict[website]["password"]
    except FileNotFoundError:
        mbox.showerror("Error", "File not found!")
    except KeyError:
        mbox.showerror("Error", "Website not found!")
    else:
        mbox.showinfo("Your data", f"E-mail: {email}"
                                   f"\nPassword: {password}")

# OBS: If you can do something easily with If/Else, so stick to it and give that a go, but if it isn't so easy, give Except a go


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_User = email_User_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_User,
            "password": password
        }
    }

    if website == "" or email_User == "" or password == "":
        mbox.showerror("Error", "Please fill all fields")
    else:
        is_ok = mbox.askokcancel(title=website, message=f"These are the details entered:"
                                                f"\nE-mail: {email_User}"
                                                f"\nPassword: {password}"
                                                f"\nIs it ok to save?")
        if is_ok:
            try:
                with open("passwords.json", "r") as data_file:
                    #Read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update old data with new data (Append)
                data.update(new_data)
                # Save updated data
                with open("passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
Email_User_label = Label(text="E-mail/Username:")
Email_User_label.grid(column=0, row=2)
Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()
email_User_entry = Entry(width=51)
email_User_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_User_entry.insert(0, "victor@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)



window.mainloop()