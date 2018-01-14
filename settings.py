"""
settings.py

Created on: 2018-01-13

Establish settings for bank_db.py
"""

import os

# Database URL and Name
DB_NAME = "bank"
DB_URL = 'aa1sbw4dz894udn.cv1nhpusk2zj.us-west-2.rds.amazonaws.com'

# Database credentials
DB_UNAME = os.environ["DB_UNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]