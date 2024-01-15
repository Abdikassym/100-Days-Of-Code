import random
import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------------- Generate words ---------------------------------------

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")

words_data = data.to_dict(orient="records")
print(words_data)

current_card = {}


def click_yes():
    global current_card
    words_data.remove(current_card)
    words_to_learn_data = pandas.DataFrame(words_data)
    words_to_learn_data.to_csv("words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_data)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# --------------------------------------- UI ---------------------------------------


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(file='card_front.png')
card_back = tkinter.PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)

language_text = canvas.create_text(400, 150, text="Press a button to", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Start", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

tick_image = tkinter.PhotoImage(file='right.png')
right_button = tkinter.Button(image=tick_image, highlightthickness=0, command=click_yes)
right_button.grid(column=1, row=1)

x_image = tkinter.PhotoImage(file='wrong.png')
wrong_button = tkinter.Button(image=x_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()







window.mainloop()
