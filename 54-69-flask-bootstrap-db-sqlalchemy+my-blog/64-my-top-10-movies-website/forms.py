from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    rating = FloatField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
