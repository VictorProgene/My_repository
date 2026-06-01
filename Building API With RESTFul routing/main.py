from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
# from random import randint
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/rand")
def rand():
    # #READ A SPECIFIC RECORD
    cafe_id = random.randint(0, 21)
    with app.app_context():
        cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()

    return jsonify(id=cafe.id,
                   name=cafe.name,
                   map_url=cafe.map_url,
                   img_url=cafe.img_url,
                   location=cafe.location,
                   has_sockets=cafe.has_sockets,
                   has_toilet=cafe.has_toilet,
                   has_wifi=cafe.has_wifi,
                   can_take_calls=cafe.can_take_calls,
                   seats=cafe.seats,
                   coffe_price=cafe.coffee_price
                   )

@app.route("/all")
def all():
    #READ ALL RECORDS
    with app.app_context():
        response = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        all_cafes = response.scalars().all()

        all_cafes_list = []
        for cafe in all_cafes:
            all_cafes_list.append({
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "has_sockets": cafe.has_sockets,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "can_take_calls": cafe.can_take_calls,
                "seats": cafe.seats,
                "coffee_price": cafe.coffee_price,
            })

        return jsonify(cafes=all_cafes_list)

@app.route("/search/")
def search():
    #READ ALL RECORDS
    with app.app_context():
        response = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        all_cafes = response.scalars().all()

        location = request.args.get("loc")

        all_cafes_list = []
        for cafe in all_cafes:
            if cafe.location == location:
                all_cafes_list.append({
                    "id": cafe.id,
                    "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "has_sockets": cafe.has_sockets,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "can_take_calls": cafe.can_take_calls,
                    "seats": cafe.seats,
                    "coffee_price": cafe.coffee_price,
                })

        if not all_cafes_list:
            all_cafes_list={"Not found":"Sorry, we don't have a cafe at this location."}
            return jsonify(Error=all_cafes_list)



        return jsonify(cafes=all_cafes_list)

#OBS: POST uses forms instead of args
# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    with app.app_context():
        # Create the record
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=request.form.get("has_toilet") == "True",
            has_wifi=request.form.get("has_wifi") == "True",
            has_sockets=request.form.get("has_sockets") == "True",
            can_take_calls=request.form.get("can_take_calls") == "True",
            coffee_price=request.form.get("coffee_price"),
        )

        db.session.add(new_cafe)
        db.session.commit()

    add_cafe = {"Success": "Successfully added a new cafe!."}
    return jsonify(Response=add_cafe)

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    #UPDAE USING ITS ID
    try:
        with app.app_context():
            cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            cafe_to_update.coffee_price = request.args.get("new_coffee_price")
            print(request.args.get("new_coffee_price"))
            db.session.commit()
        return jsonify(Response="Successfully updated the price.")
    except:
        return jsonify(Not_found="Sorry a cafe with this id is not found in the database.")


# HTTP DELETE - Delete Record
@app.route("/delete-cafe/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    #DELETE USING ITS ID
    try:
        with app.app_context():
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
            db.session.delete(cafe_to_delete)
            db.session.commit()

            if request.args.get("api-key") != "TopSecretApiKey":
                return jsonify(Error="Sorry, that's not allowed. Make sure you have the correcct api_key.")

        return jsonify(Response="Successfully deleted cafe.")
    except:
        return jsonify(Error="Sorry a cafe with this id is not found in the database.")




if __name__ == '__main__':
    app.run(debug=True)
