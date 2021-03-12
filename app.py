import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/homework")
def homework():
    return render_template("homework.html")


@app.route("/")
@app.route("/show_tasks")
def show_tasks():
    homework = mongo.db.homework.find()
    return render_template("leads.html", homework=homework)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User is already registered")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return render_template("homework.html")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check passwords match
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return render_template("homework.html")
            else:
                # passwords do not match
                flash("Username and/or password is incorrect")
                return redirect(url_for("login"))

        else: 
            # username does not exist
            flash("Username and/or password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")




@app.route("/logout")
def logout():
    flash("You are now logged out of the site")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)