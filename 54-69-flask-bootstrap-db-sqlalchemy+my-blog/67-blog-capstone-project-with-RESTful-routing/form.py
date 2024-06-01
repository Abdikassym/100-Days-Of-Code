from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class MyForm(FlaskForm):
    title = StringField(label="Blog post title", validators=[DataRequired()])
    subtitle = StringField(label="Blog post subtitle", validators=[DataRequired()])
    author = StringField(label="Author's name", validators=[DataRequired()])
    img_url = StringField(label="Background image URL", validators=[DataRequired()])
    body = CKEditorField(label="Blog post Text", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")
