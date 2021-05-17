
from flask import Blueprint, request, jsonify, render_template, redirect, flash

from python.service import get

form = Blueprint("form", __name__)

@form.route("/contact/form.json")
def form_api():
    name = request.args.get("name")
    email = request.args.get("email") 

    results = get(name=name, email=email)
    if results:
        return jsonify(results)
    else:
        return jsonify({"message":"Invalid. Please try again."}), 404


@form.route("/contact/form")
def contact_form():
    print("Contact Form...")
    return render_template("contact.html")

@form.route("/thanks", methods=["GET", "POST"])
def thankyou():

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    name = request_data.get("name")
    email = request_data.get("email")

    results = get(name=name, email=email)
    if results:
        flash("Contact Form Sent Successfully!", "success")
        return render_template("thanks.html", name=name, email=email, results=results)
    else:
        flash("Error. Please try again!", "danger")
        return redirect("/contact/form")
