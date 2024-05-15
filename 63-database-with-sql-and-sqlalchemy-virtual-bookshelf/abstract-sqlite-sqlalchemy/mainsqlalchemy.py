from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# create a table
with app.app_context():
    db.create_all()

# create a record (add row) -> commented in order to not break a code by creating the same record everytime I run a code
# with app.app_context():
#     new_book = Book(title='31 Harry Potter', author='J.K.Rowling', rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()


# read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    # for book in all_books:
    #     print(book.title)


# read a particular record by query (by title)
with app.app_context():
    book_by_title = db.session.execute(db.select(Book).where(Book.title == "21 Harry Potter")).scalar()
    book_by_id = db.session.execute(db.select(Book).where(Book.id == 5)).scalar()
    # print(book_by_title.title, book_by_title.id)
    # print(book_by_id.title, book_by_id.id)


# update a particular record by query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter And The Chamber Of Secrets")).scalar()
    book_to_update.title = "Harry Potter And The Chamber Of Secrets"
    db.session.commit()


# update a particular record by PRIMARY_KEY
book_id = 1
with app.app_context():
    book_to_update_by_id = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update_by_id.title = "Harry Potter And The Philosopher's Gem"
    db.session.commit()


# delete a particular record by PRIMARY_KEY
# book_to_delete_id = 5  # -> commented so that its not giving error every time, since I am trying to delete deleted book-object
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_to_delete_id)).scalar()
#     db.session.delete(book_to_delete)
#     db.session.commit()
