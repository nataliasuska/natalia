
"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, request

import stripe



STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", default="PK_OOPS") # client-side
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", default="SK_OOPS") # server-side
stripe.api_key = STRIPE_SECRET_KEY

app = Flask(__name__,
            static_url_path='',
            static_folder='.')

YOUR_DOMAIN = 'https://nataliasuska.herokuapp.com/checkout'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 65,
                        'product_data': {
                            'name': '1-Hour Photoshoot with Natalia',
                            'images': ['https://github.com/nataliasuska/natalia/blob/main/website/templates/portfolio/cover.jpg?raw=true'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=https://nataliasuska.herokuapp.com/success.html',
            cancel_url=https://nataliasuska.herokuapp.com/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(port=4242)
