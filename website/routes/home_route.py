from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME PAGE")
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT NATALIA")
    return render_template("about.html")
