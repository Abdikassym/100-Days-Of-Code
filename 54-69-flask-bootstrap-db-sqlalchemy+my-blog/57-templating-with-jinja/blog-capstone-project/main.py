import requests
from flask import Flask, render_template
from post import Post


app = Flask(__name__)

blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blogs_url)
blogposts = response.json()
post_objects = []

for blog in blogposts:
    id = blog['id']
    body = blog['body']
    title = blog['title']
    subtitle = blog['subtitle']
    post_object = Post(post_id=id, subtitle=subtitle, title=title, body=body)
    post_objects.append(post_object)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for post in post_objects:
        if post.id == post_id:
            requested_post = post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
