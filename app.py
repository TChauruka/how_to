import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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
@app.route("/get_hows/")
def get_hows():
    hows = list(mongo.db.hows.find())
    return render_template("get_hows.html", hows=hows)


@app.route("/category/<category_name>")
def category(category_name):
    # url_for("category", category_name="social") --> /category/social
    hows = list(mongo.db.hows.filter({"category_name": category_name}))
    return render_template("category_detail.html", category_name=category_name, hows=hows)


@app.route("/get_categories/")
def get_categories():
    categories = list(mongo.db.categories.find())
    return render_template("get_categories.html", categories=categories)


@app.route("/add_category/", methods=["GET","POST"])
def add_category():
    if request.method=="POST":
        category ={
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category )
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>",methods=["POST","GET"])
def edit_category(category_id):
    if request.method == "POST":
        submit ={
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id":ObjectId(category_id)}, submit)
        flash("Category Successfuly Updated")
        return redirect(url_for("get_categories"))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html" ,category=category)

@app.route("/register/", methods=["GET","POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    #remove user from session cookies
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_hows/", methods=["Get","POST"])
def add_hows():
    if request.method == "POST" :
        task = {
            "category_name": request.form.get("category_name"),
            "hows_title": request.form.get("hows_title"),
            "hows_description": request.form.get("hows_description"),
            "created_by": session["user"]
        }
        mongo.db.hows.insert_one(task)
        flash("How To Successfully Added")
        return redirect(url_for("get_hows"))

    categories = mongo.db.categories.find().sort("category_name",1)
    return render_template("add_hows.html", categories = categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
