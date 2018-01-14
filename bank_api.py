"""
Flask API for accessing and making transactions on (dummy) banking data.
This application enforces access control - every transaction must be sent with
a valid crypto-ticket from the auth server.
"""

from flask_sslify import SSLify
from flask import Flask, json, request
from bank_db import BankDBConnection
import psycopg2

app = Flask(__name__)
application = app
sslify = SSLify(app)

bank_db = BankDBConnection()


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

    results = bank_db.execute(
        """
        SELECT a.account_id, u, a.acct_amount
        FROM accounts a INNER JOIN account_type atype ON a.user_id = u.user_id WHERE a.user_id = %s AND atype.account_type LIKE %s;
        """,
        (uid, ))
    amount_list = []

    if results is not None:
        for acct_amount in results:
            amount_list.append(acct_amount)
    else:
        return None

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
