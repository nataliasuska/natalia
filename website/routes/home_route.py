from flask import Blueprint, render_template, Flask, request, flash
from form import ContactForm
from flask_mail import Mail, Message
import smtplib
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def home():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        return render_template("home.html", msg_sent=True)
    return render_template("home.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage:{message}"
    with smtplib.SMTP("smtp.zoho.eu") as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(EMAIL, EMAIL, email_message)

if __name__=="__main__":
    home_routes.run(debug=True)

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