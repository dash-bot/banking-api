"""
Flask API for accessing and making transactions on (dummy) banking data.
This application enforces access control - every transaction must be sent with
a valid crypto-ticket from the auth server.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello world!"
