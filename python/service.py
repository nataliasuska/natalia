
import os
import json
from dotenv import load_dotenv
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python import APP_ENV

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

load_dotenv()


def sett():
    if APP_ENV == "production":
        name = input("Please input a name: ")
        email = input("Please input an email: ")
    else:
        exit


def send_email(subject=" This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e.message)
        return None

if __name__ == "__main__":

    print(f"Running form in {APP_ENV.upper()} ...")

    name, email = sett()

    todays_date = date.today().strftime('%A, %B %d, %Y')

    html = ""
    html += f"<h3>Good Morning!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{todays_date}</p>"

    html += f"<h4>Email from {name}</h4>"
    html += f"<p>{name}'s email is {email}</p>"

    send_email(subject="Art Commission", html=html)
