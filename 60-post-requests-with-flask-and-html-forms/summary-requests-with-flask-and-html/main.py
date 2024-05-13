from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def login():
    return f"<h1>Name: {request.form['name']}</h1>" \
           f"<h1>Password: {request.form['password']}</h1>"


if __name__ == "__main__":
    app.run(debug=True)


