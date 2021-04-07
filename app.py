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


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check passwords match
            if (check_password_hash(existing_user["password"], request.form.get("password"))):
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


@app.route("/homework")
def homework():
    if 'user' in session:
        return render_template("homework.html", homework=homework)


@app.route("/lead_tasks")
def lead_tasks():
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("leads.html", homework=homework, user=user)


@app.route("/musicteam_tasks")
def musicteam_tasks():
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("musicteam.html", homework=homework, user=user)


@app.route("/wholechorus_tasks")
def wholechorus_tasks():
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template(
            "wholechorus.html", homework=homework, user=user)


@app.route("/tenor_tasks")
def tenor_tasks():
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("tenor.html", homework=homework, user=user)


@app.route("/bari_tasks")
def bari_tasks():
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("bari.html", homework=homework, user=user)


@app.route("/bass_tasks")
def bass_tasks():
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("bass.html", homework=homework, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        is_musicteam = "on" if request.form.get("is_musicteam") else "off"
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User is already registered")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if password != confirm_password:
            flash("Passwords do not match")
            return render_template("register.html")

        if password == confirm_password:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "is_musicteam": is_musicteam
            }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return render_template("homework.html")

    return render_template("register.html")


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = {
            "section_name": request.form.get("section_name"),
            "song_name": request.form.get("song_name"),
            "task_title": request.form.get("task_title"),
            "due_date": request.form.get("due_date"),
            "task_description": request.form.get("task_description"),
            "created_by": session["user"]
        }
        mongo.db.homework.insert_one(task)
        flash("New Task Added Successfully")
        return redirect(url_for("homework"))

    sections = mongo.db.sections.find().sort("section_name", 1)
    return render_template("add_tasks.html", sections=sections)


@app.route("/edit_task/<homework_id>", methods=["GET", "POST"])
def edit_task(homework_id):
    if request.method == "POST":
        submit = {
            "section_name": request.form.get("section_name"),
            "song_name": request.form.get("song_name"),
            "task_title": request.form.get("task_title"),
            "due_date": request.form.get("due_date"),
            "task_description": request.form.get("task_description"),
            "created_by": session["user"]
        }
        mongo.db.homework.update({"_id": ObjectId(homework_id)}, submit)
        flash("Task Successfully Updated")
        return redirect(url_for("homework"))

    homework = mongo.db.homework.find_one({"_id": ObjectId(homework_id)})
    sections = mongo.db.sections.find().sort("section_name", 1)
    return render_template(
        "edit_task.html", homework=homework, sections=sections)


@app.route("/delete_task/<homework_id>")
def delete_task(homework_id):
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("homework"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
