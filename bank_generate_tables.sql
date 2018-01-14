/* generate_tables.sql
 *
 * Created on: 2018-01-13
 *
 * Generate SQL tables for AWS RDS PostgreSQL database to store bank info.
 */


CREATE TABLE users (
  user_id    INT PRIMARY KEY,
  first_name TEXT,
  last_name  TEXT,
  phone_num  BIGINT,
  email      TEXT
);

CREATE TABLE account_type (
  account_type_id INT PRIMARY KEY,
  account_type    TEXT
);

CREATE TABLE accounts (
  account_id   INT PRIMARY KEY,
  user_id      INT REFERENCES Users (user_id),
  account_type INT, -- View AccountType to determine account type
  acct_amount  REAL,
  FOREIGN KEY (user_id) REFERENCES Users (user_id),
  FOREIGN KEY (account_type) REFERENCES account_type (account_type_id)
);

CREATE TABLE transaction_type (
  transaction_type_id INT PRIMARY KEY,
  transaction_type    TEXT
);

CREATE TABLE transactions (
  transaction_id      INT,
  timestamp           TIMESTAMP WITH TIME ZONE,
  transaction_type    INT, -- View TransactionType to determine transaction type
  sender_id           INT,
  sender_account_id   INT,
  receiver_id         INT,
  receiver_account_id INT,
  transaction_amount  REAL,
  FOREIGN KEY (transaction_type) REFERENCES transaction_type (transaction_type_id),
  FOREIGN KEY (sender_id) REFERENCES Users (user_id),
  FOREIGN KEY (receiver_id) REFERENCES Users (user_id),
  FOREIGN KEY (sender_account_id) REFERENCES Accounts (account_id),
  FOREIGN KEY (receiver_account_id) REFERENCES Accounts (account_id)
);

