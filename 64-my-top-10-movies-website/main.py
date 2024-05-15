import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import requests
from forms import EditForm, AddForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

API_KEY = os.environ["MOVIES_API_KEY"]
API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
DETAILS_API_ENDPOINT = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# CREATE TABLE
with app.app_context():
    db.create_all()

# add a movie to db
# with app.app_context():
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    movie_list = [movie for movie in all_movies]
    for rank in range(len(movie_list)):
        movie_list[rank].ranking = len(movie_list) - rank
        db.session.commit()
    return render_template("index.html", movies=movie_list)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie_to_edit = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie_to_edit, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {
            "query": form.title.data,
            "include_adult": False,
            "language": "en-US"
        }
        headers = {
            "accept": "application.json",
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url=API_ENDPOINT, params=params, headers=headers).json()
        movies = response["results"]
        return render_template('select.html', movies=movies)
    return render_template("add.html", form=form)


@app.route('/gather_data', methods=["GET", "POST"])
def get_movie_data():
    movie_id = request.args.get('id')
    headers = {
        "accept": "application.json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url=f"{DETAILS_API_ENDPOINT}/{movie_id}", headers=headers).json()

    title = response["title"]
    img_url = f"{MOVIE_DB_IMAGE_URL}/{response['poster_path']}"
    year = response["release_date"].split("-")[0]
    description = response["overview"]

    new_movie = Movie(
        title=title,
        img_url=img_url,
        year=year,
        description=description
    )
    db.session.add(new_movie)
    db.session.commit()

    movie_to_edit = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar()
    movie_id = movie_to_edit.id

    return redirect(url_for('edit', id=movie_id))


if __name__ == '__main__':
    app.run(debug=True)
