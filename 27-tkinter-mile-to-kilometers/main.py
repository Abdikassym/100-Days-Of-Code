from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="Label Text", font=("Calibri", 32))
my_label.grid(column=0, row=0)

my_label["text"] = "Hello"
my_label.config(text="Hello")

click_amount = 0


# Button
def button_clicked():
    global click_amount
    click_amount += 1
    my_label["text"] = f"Button got clicked {click_amount} times!"


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


# Entry
def change_the_label():
    my_label["text"] = user_input.get()


user_input = Entry(width=20)
user_input.grid(column=3, row=2)
button.config(command=change_the_label)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)






window.mainloop()
