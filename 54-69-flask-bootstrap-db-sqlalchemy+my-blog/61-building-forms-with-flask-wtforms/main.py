from flask import Flask, render_template, request
from form import MyForm
import os
from flask_bootstrap import Bootstrap5
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)


