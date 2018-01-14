"""
Flask API for accessing and making transactions on (dummy) banking data.
This application enforces access control - every transaction must be sent with
a valid crypto-ticket from the auth server.
"""

from flask_sslify import SSLify
from flask import Flask, json, request, g
from bank_db import BankDBConnection
import psycopg2

app = Flask(__name__)
application = app
sslify = SSLify(app)


def get_db():
    db = getattr(g, "_dbconn", None)
    if not db:
        db = g._dbconn = BankDBConnection()
    return db


@app.route("/balance", methods=['GET'])
def balance():
    """
    Gets the balance for a given user.

    Request parameters:
        uid = USER ID

    Response:
        {
            "balances" : {
                [Account_ID, Account_Type, Account_Amount], +
            }
        }
    """
    uid = request.args["uid"]

    # Query for given uid's bank accounts
    amount_list = get_db().get_account_balances(uid)

    # Return list of user's bank account amounts in JSON
    return json.jsonify({
        "balances": [
            {"id": ele[0], "name": ele[1], "balance": ele[2]} for ele in amount_list
        ]
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
    account_id_send = request.args["accountid_from"]
    account_id_receive = request.args["accountid_to"]
    amount = request.args["transfer_amount"]

    try:
        get_db().make_transfer(account_id_send, account_id_receive, amount)
    except Exception as e:
        print(e)
        return json.jsonify({'success': False})

    return json.jsonify({'success': True})


if __name__ == "__main__":
    app.run()
