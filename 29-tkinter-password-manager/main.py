import json
import tkinter
import random
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "="]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def generate_password():
    final_password = ""
    for letter in range(10):
        if letter % 2 == 0:
            final_password += random.choice(letters)
        else:
            random_letter = random.choice(letters)
            final_password += random_letter.upper()
    for symbol in range(2):
        final_password += random.choice(symbols)
    for number in range(3):
        final_password += str(random.choice(numbers))

    final_password = list(final_password)
    random.shuffle(final_password)
    final_password = "".join(final_password)
    password_entry.delete(0, "end")
    password_entry.insert(0, final_password)
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    password = password_entry.get()
    website = website_entry.get()
    email_username = email_username_entry.get()

    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(password) == 0 or len(email_username) == 0 or len(website) == 0:
        messagebox.showerror(title="Error", message="No empty fields allowed!")
    else:
        # with open("data.json", mode="r") as data_file:
        #     data = json.load(data_file)
        #     data.update(new_data)

        with open("data.json", mode="r") as data_file:
            # Reading an old data
            data = json.load(data_file)
            # Entering and updating that old data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # Saving the updated data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

        messagebox.showinfo(title="Success!", message="Data has been saved.")

# ----------------------------) UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

logo_img = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = tkinter.Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = tkinter.Entry(width=50)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=32)
password_entry.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=42, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()
