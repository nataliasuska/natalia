"""
Python 3.6 or newer required.
"""
import json
import os
from website.routes.stripe_routes import STRIPE_SECRET_KEY
import stripe
from dotenv import load_dotenv()

load_dotenv()
stripe.api_key = STRIPE_SECRET_KEY

#From https://stripe.com/docs/payments/integration-builder

from flask import Flask, render_template, jsonify, request


app = Flask(__name__, static_folder=".",
            static_url_path="", template_folder=".")


def calculate_order_amount(items):
    return 65


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run()