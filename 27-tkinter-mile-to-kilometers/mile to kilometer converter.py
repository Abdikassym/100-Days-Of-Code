from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)


def convert():
    mile = float(distance_entry.get())
    result["text"] = mile * 1.6


text = Label(text="is equal to")
text.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

Km = Label(text="Km")
Km.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

distance_entry = Entry()
distance_entry.focus()
distance_entry.insert(END, "0")
distance_entry.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
