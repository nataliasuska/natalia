from flask import Flask
import os
from dotenv import load_dotenv

from website.routes.home_route import home_routes
from website.routes.stripe_routes import stripe_routes


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(home_routes)
    app.register_blueprint(stripe_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)