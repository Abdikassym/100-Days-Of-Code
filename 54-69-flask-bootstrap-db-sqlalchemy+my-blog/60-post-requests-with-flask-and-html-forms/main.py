from flask import Flask, render_template, request
import requests
import smtplib

my_email = "abdikasymt@gmail.com"
password = "ojdt wgth vtin iatc"

app = Flask(__name__)

posts_json = requests.get(url="https://api.npoint.io/8af85767f0aff7e3d92d").json()


@app.route('/')
def get_home():
    return render_template("index.html", posts=posts_json)


@app.route('/contact', methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_phone = request.form["phone"]
        user_message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=user_email,
                                msg=f"Subject:{user_name} contacted you via Blog!\n\n"
                                    f"Name: {user_name}\n"
                                    f"Phone: {user_phone}\n"
                                    f"Email: {user_email}\n"
                                    f"Message: {user_message}")
            print("message sent")
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html")


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def get_post(post_id):
    return render_template("post.html", post=posts_json[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)

