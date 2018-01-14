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

    def close(self):
        self._conn.close()
