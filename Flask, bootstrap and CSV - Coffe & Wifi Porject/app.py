from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from dotenv import load_dotenv
import os
import csv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location on google maps', validators=[DataRequired(), URL(message="Please enter a valid URL")])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Opening Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField(
        'Coffee Rating',
        choices=[
            ('☕', '☕'),
            ('☕☕', '☕☕'),
            ('☕☕☕', '☕☕☕'),
            ('☕☕☕☕', '☕☕☕☕'),
            ('☕☕☕☕☕', '☕☕☕☕☕'),
        ],
        validators=[DataRequired()]
    )

    wifi = SelectField(
        'Wifi Strength Rating',
        choices=[
            ('✘', '✘'),
            ('💪', '💪'),
            ('💪💪', '💪💪'),
            ('💪💪💪', '💪💪💪'),
            ('💪💪💪💪', '💪💪💪💪'),
        ],
        validators=[DataRequired()]
    )

    charging = SelectField(
        'Charging Spots Rating',
        choices=[
            ('✘', '✘'),
            ('🔌', '🔌'),
            ('🔌🔌', '🔌🔌'),
            ('🔌🔌🔌', '🔌🔌🔌'),
            ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Add cafe')


# all Flask routes below
@app.route('/home')
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", mode="a", encoding="utf-8") as file:

            file.write(
                f"{form.cafe.data},"
                f"{form.location.data},"
                f"{form.open.data},"
                f"{form.close.data},"
                f"{form.rating.data},"
                f"{form.wifi.data},"
                f"{form.charging.data}\n"
            )

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
