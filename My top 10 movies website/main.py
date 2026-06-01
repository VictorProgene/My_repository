from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your key'
API_KEY = "Your API KEY"
API_READ_ACCESS_TOKEN = "Your API Token"
Bootstrap5(app)

#--------------------------------------------CREATE DB----------------------------------------------------
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# The SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies-collection.db"
# initialize the app with the extension
db.init_app(app)


#-----------------------------------------------------CREATE TABLE---------------------------------------------
class Movie(db.Model):

    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str] = mapped_column(
        String(250),
        unique=True,
        nullable=False
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(500),
        unique=False,
        nullable=False
    )

    rating: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    ranking: Mapped[int] = mapped_column(
        Integer,
        unique=False,
        nullable=False
    )

    review: Mapped[str] = mapped_column(
        String(250),
        nullable=False
    )

    img_url: Mapped[str] = mapped_column(
        String(250),
        unique=True,
        nullable=False
    )



#---------------------------------MANUALY CREATE A NEW RECORD----------------------------------------
with app.app_context():
    #Create the DB
    db.create_all()
#
#     #Create the record
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
# #
#     db.session.add(new_movie)
#     db.session.commit()
#
#     db.session.add(second_movie)
#     db.session.commit()

#-------------------------------FORM-----------------------------------

class EditForm(FlaskForm):
    rating_field = StringField('Your rating out of 10 e.g.7.5', validators=[DataRequired()])
    review_field = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    movie_title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField("Add movie")



#--------------------------------SITE----------------------------------


@app.route("/")
def home():
    #READ ALL RECORDS
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.title))
        all_movies = result.scalars().all()
        all_movies = sorted(all_movies, key=lambda m: m.ranking, reverse=True)

        names_rating_dict = {movie.title:movie.rating for movie in all_movies}
        print(names_rating_dict)

        ranking = sorted(names_rating_dict.items(), key=lambda item: item[1], reverse=True)

        for posicao, (filme, nota) in enumerate(ranking, start=1):
            print(f"{posicao}º lugar: {filme} - {nota}")

            # # #UPDATE A SPECIFIC RECORD
            with app.app_context():
                movie_to_update = db.session.execute(db.select(Movie).where(Movie.title == filme)).scalar()
                movie_to_update.ranking = posicao
                db.session.commit()



        # for movie in all_movies:
        #     # print(movie.title, movie.description, movie.rating)
        #     names_rating_dict = {movie.title:movie.rating}
        #     print(names_rating_dict)
    return render_template("index.html", all_movies=all_movies)

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    form = EditForm()
    form.validate_on_submit()
    movie_id = request.args.get("movie_id", type=int)
    real_movie_name = request.args.get("real_movie_name", type=str)
    print(movie_id)
    print(real_movie_name)

    if form.validate_on_submit():

        # #UPDAE USING ITS ID
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
            movie_to_update.rating = form.rating_field.data
            db.session.commit()
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
            movie_to_update.review = form.review_field.data
            db.session.commit()


        print(form.rating_field.data)  # Print the info (email) from form submited
        print(form.review_field.data)  # Print the info (email) from form submited
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get("movie_id", type=int)
    #DELETE USING ITS ID
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    print(form.movie_title.data)

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": API_KEY,
        "query": form.movie_title.data
    }

    if form.validate_on_submit():
        response = requests.get(url, params=params)
        data = response.json()
        length = len(data["results"])
        movie_titles_list = [movie["title"] for movie in data["results"]]
        print(movie_titles_list)

        return render_template("select.html", data=data, length=length, movie_titles_list=movie_titles_list)

    return render_template("add.html", form=form)

@app.route("/select/<real_movie_name>", methods=["GET", "POST"])
def select(real_movie_name):

    print(real_movie_name)
    url = "https://api.themoviedb.org/3/search/movie"
    #
    params = {
        "api_key": API_KEY,
        "query": real_movie_name
    }
    with app.app_context():
        response = requests.get(url, params=params)

        data = response.json()


        print(data["results"][0]["title"])

        print(int(data["results"][0]["release_date"][:4]))

        print(data["results"][0]["vote_average"])

        print(data["results"][0]["overview"])

        print(
            f"https://image.tmdb.org/t/p/w500{data['results'][0]['poster_path']}"
        )
        #Create the record
        new_movie = Movie(
            title=data["results"][0]["title"],
            year=int(data["results"][0]["release_date"][:4]),
            description=data["results"][0]["overview"],
            rating=data["results"][0]["vote_average"],
            ranking=2,
            review="Minha opnião",
            img_url=f"https://image.tmdb.org/t/p/w500{data['results'][0]['poster_path']}"
        )

        db.session.add(new_movie)
        db.session.commit()

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
