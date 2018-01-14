"""
bank_db.py

Created on: 2018-01-13

Establish bank's database connection class for use in
bank_api.py when communicating and interacting with Bank database.
"""

import psycopg2
from settings import DB_NAME, DB_URL, DB_UNAME, DB_PASSWORD


class BankDBConnection(object):
    def __init__(self):
        self._conn = psycopg2.connect(dbname=DB_NAME, user=DB_UNAME, password=DB_PASSWORD, host=DB_URL)

    def init_query(self):
        self._cur = self._conn.cursor()

    def get_account_balances(self, uid):
        cur = self._conn.cursor()

        cur.execute(
            """
            SELECT a.account_id, atype.account_type, a.acct_amount
            FROM accounts a INNER JOIN account_type atype ON a.account_type = atype.account_type_id 
            WHERE a.user_id = %s;
            """,
            (uid,))

        return cur.fetchall()

    def close(self):
        self._conn.close()
