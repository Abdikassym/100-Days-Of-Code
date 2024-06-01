from flask import Flask, render_template
import requests

app = Flask(__name__)

posts_json = requests.get(url="https://api.npoint.io/8af85767f0aff7e3d92d").json()


@app.route('/')
def get_home():
    return render_template("index.html", posts=posts_json)


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def get_post(post_id):
    return render_template("post.html", post=posts_json[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)

