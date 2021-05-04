from flask import Flask, request, jsonify

web = Flask(__name__)

@web.route("/")
def test():
    return "It works!"