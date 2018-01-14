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
                [Account_ID, Account_Type, Account_Amount], +
            }
        }
    """
    uid = request.args["uid"]

    # Query for given uid's bank accounts
    results = bank_db.execute(
        """
        SELECT a.account_id, atype.account_type, a.acct_amount
        FROM accounts a INNER JOIN account_type atype ON a.account_type = atype.account_type_id WHERE a.user_id = %s;
        """,
        (uid))

    amount_list = []

    if results is not None:
        for acct_amount in results:
            amount_list.append(acct_amount)
    else:
        return None

    # Return list of user's bank account amounts in JSON
    return json.jsonify({
        "balances": {
            amount_list
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
