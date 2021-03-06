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
    """
    Function for logging in existing users. New users can follow
    the link to register a new account from here.
    """
    if request.method == "POST":
        # check username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check passwords match
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
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
    """
    Function to allow users to logout of the site.
    """
    flash("You are now logged out of the site")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/homework")
def homework():
    """
    Function for loading the home page. 6 cards on this page will link
    to the individual section pages where the sections can see the tasks
    that have been allocated to them.
    """
    if 'user' in session:
        return render_template("homework.html", homework=homework)


@app.route("/lead_tasks")
def lead_tasks():
    """
    Function for showing members of the lead section the tasks that have
    been allocated to their section. Music Team members can also add, edit
    and delete tasks from this page.
    """
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("leads.html", homework=homework, user=user)


@app.route("/musicteam_tasks")
def musicteam_tasks():
    """
    Function for showing members of the music team the tasks that have
    been allocated to their section. Music Team members can also add, edit
    and delete tasks from this page.
    """
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("musicteam.html", homework=homework, user=user)


@app.route("/wholechorus_tasks")
def wholechorus_tasks():
    """
    Function for showing members the tasks that have been set for the whole
    chorus. Music Team members can also add, edit and delete tasks from
    this page.
    """
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template(
            "wholechorus.html", homework=homework, user=user)


@app.route("/tenor_tasks")
def tenor_tasks():
    """
    Function for showing members of the tenor section the tasks that have
    been allocated to their section. Music Team members can also add, edit
    and delete tasks from this page.
    """
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("tenor.html", homework=homework, user=user)


@app.route("/bari_tasks")
def bari_tasks():
    """
    Function for showing members of the bari section the tasks that have
    been allocated to their section. Music Team members can also add, edit
    and delete tasks from this page.
    """
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("bari.html", homework=homework, user=user)


@app.route("/bass_tasks")
def bass_tasks():
    """
    Function for showing members of the bass section the tasks that have
    been allocated to their section. Music Team members can also add, edit
    and delete tasks from this page.
    """
    if 'user' in session:
        homework = mongo.db.homework.find()
        user = mongo.db.users.find_one({"username": session['user']})
        return render_template("bass.html", homework=homework, user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function for allowing new members to register on the site. Also checks if
    the username is already registered on the site. Existing members can also
    follow the link to log in from this page.
    """
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
    """
    Members of the music team can add tasks for their section from this page.
    The drop down menu allows the correct section to be selected for the task.
    """
    user = mongo.db.users.find_one({"username": session['user']})
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
    return render_template("add_tasks.html", sections=sections, user=user)


@app.route("/edit_task/<homework_id>", methods=["GET", "POST"])
def edit_task(homework_id):
    """
    Function that enables members of the music team to edit any tasks that need
    to be changed.
    """
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


@app.route("/delete_task_bass/<homework_id>")
def delete_task_bass(homework_id):
    """
    Function that enables bass section tasks to be deleted by members of the
    music team. Once deleted they will be routed back to the bass section page.
    """
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("bass_tasks"))


@app.route("/delete_task_bari/<homework_id>")
def delete_task_bari(homework_id):
    """
    Function that enables bari section tasks to be deleted by members of the
    music team. Once deleted they will be routed back to the bari section page.
    """
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("bari_tasks"))


@app.route("/delete_task_lead/<homework_id>")
def delete_task_lead(homework_id):
    """
    Function that enables lead section tasks to be deleted by members of the
    music team. Once deleted they will be routed back to the lead section page.
    """
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("lead_tasks"))


@app.route("/delete_task_tenor/<homework_id>")
def delete_task_tenor(homework_id):
    """
    Function that enables tenor section tasks to be deleted by members of the
    music team. Once deleted they will be routed back to the tenor section
    page.
    """
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("tenor_tasks"))


@app.route("/delete_task_musicteam/<homework_id>")
def delete_task_musicteam(homework_id):
    """
    Function that enables music team tasks to be deleted by members of the
    music team. Once deleted they will be routed back to the music team section
    page.
    """
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("musicteam_tasks"))


@app.route("/delete_task_wholechorus/<homework_id>")
def delete_task_wholechorus(homework_id):
    """
    Function that enables tasks that have been set for the whole chorus to be
    deleted by members of the music team. Once deleted they will be routed
    back to the whole chorus page.
    """
    mongo.db.homework.remove({"_id": ObjectId(homework_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("wholechorus_tasks"))


@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a custom 404 error page with a link
    to take the user back to homework.html
    """
    return render_template('404.html', error=error), 404


@app.errorhandler(400)
def server_error(error):
    """
    Renders a custom 400 error page with a link
    to take the user back to homework.html
    """
    return render_template('400.html', error=error), 400


@app.errorhandler(401)
def bad_request(error):
    """
    Renders a custom 401 error page with a link
    to take the user back to homework.html
    """
    return render_template('401.html', error=error), 401


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Renders a custom 405 error page with a link
    to take the user back to homework.html
    """
    return render_template('405.html', error=error), 405


@app.errorhandler(500)
def server_error(error):
    """
    Renders a custom 500 error page with a link
    to take the user back to homework.html
    """
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
