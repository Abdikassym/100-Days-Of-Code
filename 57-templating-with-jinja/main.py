import datetime
import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

agify_endpoint = "https://api.agify.io?name="
genderize_endpoint = "https://api.genderize.io?name="


@app.route("/")
def hello():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", random_number=random_number, current_year=year)


@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(url=f"{genderize_endpoint}{name}").json()['gender']
    age_response = requests.get(url=f"{agify_endpoint}{name}").json()['age']
    return render_template("guess.html", name=name, gender=gender_response, age=age_response)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
