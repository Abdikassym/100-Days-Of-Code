from flask import Flask
import random

app = Flask(__name__)
answer = random.randint(0, 9)
print(answer)


@app.route("/")
def hello():
    return "<h1 style='text-align: center'>Guess the number between 0 and 9!</h1>" \
           "<img style='margin-left: auto; margin-right: auto; width: 30%; display: block;' src='https://media1.tenor.com/m/k_UsDt9xfWIAAAAC/i-will-eat-you-cat.gif'>"


@app.route("/<int:number>")
def guess_number(number):
    if number == answer:
        return "<h1 style='text-align: center'>You guessed it right!</h1>" \
               "<img style='margin-left: auto; margin-right: auto; width: 30%; display: block;' src='https://media.tenor.com/CnP64S7lszwAAAAi/meme-cat-cat-meme.gif'>"
    elif number < answer:
        return "<h1 style='text-align: center'>Your number number is lower</h1>" \
               "<img style='margin-left: auto; margin-right: auto; width: 30%; display: block;' src='https://media1.tenor.com/m/yNMGjXsoYGUAAAAd/cat-cats.gif'>"

    else:
        return "<h1 style='text-align: center'>Your number is higher</h1>" \
               "<img style='margin-left: auto; margin-right: auto; width: 30%; display: block;' src='https://media1.tenor.com/m/jmdUY9TVm5IAAAAd/cat-the-voices.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
