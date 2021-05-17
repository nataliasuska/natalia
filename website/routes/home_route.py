from flask import Blueprint, render_template, Flask, request, smtplib
import os

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME")
    return render_template("home.html")

@home_routes.route("/paintings")
def paintings():
    print("PAINTINGS")
    return render_template("paintings.html")

@home_routes.route("/drawings")
def drawings():
    print("DRAWINGS")
    return render_template("drawings.html")

@home_routes.route("/photography")
def photography():
    print("PHOTOGRAPHY")
    return render_template("photography.html")