from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time Ex: 2PM', validators=[DataRequired()])
    closing_time = StringField('Closing Time Ex: 4AM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=["✘", "☕️", "☕☕️️", "☕️☕️☕️", "☕☕️☕️☕️️", "☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices=["✘", "💪", "💪💪️", "💪💪💪️", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_outlet = SelectField('Power Sockets Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        location_url = form.location_url.data
        open_time = str(form.open_time.data)
        closing_time = str(form.closing_time.data)
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_outlet = form.power_outlet.data
        with open("cafe-data.csv", mode="a", encoding="utf-8") as file:
            file.writelines(f"\n{cafe_name},{location_url}, {open_time}, {closing_time}, {coffee_rating}, {wifi_rating}, {power_outlet}")
            return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
