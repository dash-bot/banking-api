"""
Flask API for accessing and making transactions on (dummy) banking data.
This application enforces access control - every transaction must be sent with
a valid crypto-ticket from the auth server.
"""

from flask import Flask, json, request

app = Flask(__name__)


@app.route("/balance", methods=['GET'])
def balance():
    """
    Gets the balance for a given user.

    Request parameters:
        uid = USER ID

    Response:
        {
            "balances" : {
                (ACCOUNT_ID: ${balance}, )+
            }
        }
    """
    uid = request.args["uid"]
    # TODO: verify uid

    return json.jsonify({
        "balances": {
            1: 2000.0,
            2: 12.0
        }
    })


@app.route("/transfer", methods=["POST"])
def transfer():
    """
    Request a transfer between bank accounts.

    Request parameters:
        accountid_from: Account ID to send from.
        accountid_to: Account ID to send to.

    Response parameters:
        { "error" : None or error message }
    """
    return "Not implemented."


if __name__ == "__main__":
    app.run()
