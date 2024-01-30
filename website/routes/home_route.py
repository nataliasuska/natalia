from flask import Blueprint, render_template, Flask, request, redirect



home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME")
    return render_template("home.html")

@home_routes.route("/photography")
def photography():
    print("PHOTOGRAPHY")
    return render_template("photography.html")

@home_routes.route("/paintings")
def paintings():
    print("PAINTINGS")
    return render_template("paintings.html")

@home_routes.route("/drawings")
def drawings():
    print("DRAWINGS")
    return render_template("drawings.html")

@home_routes.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)
if __name__ == '__main__':
    home_routes.run(debug = True)
