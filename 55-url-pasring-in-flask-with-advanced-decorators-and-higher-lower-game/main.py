from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_func():
        return f"<b>{function()}</b>"
    return wrapper_func


def make_emphasis(function):
    def wrapper_func():
        return f"<em>{function()}</em>"
    return wrapper_func


def make_underlined(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return "Bye, World!"


@app.route("/username/<name>")
def hello_name(name):
    return f"Hello, {name}"


@app.route("/username/<name>/<age>")
def hello_age(name, age):
    return f"Hello, {name}, you are {age} years old"


@app.route('/kitten')
def kitten():
    return """<h1 style="text-align: center;">This is kitten</h1>
              <img style="width: 200px;" src="https://media1.tenor.com/m/bKZVPJDnlIYAAAAd/kitten-sleeping.gif">"""


if __name__ == "__main__":
    app.run(debug=True)
