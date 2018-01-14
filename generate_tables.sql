/* generate_tables.sql
 *
 * Created on: 2018-01-13
 *
 * Generate SQL tables for AWS PostgreSQL database to store bank info.
 */


CREATE TABLE Users (
  user_id    SERIAL PRIMARY KEY,
  pwd        TEXT,
  first_name TEXT,
  last_name  TEXT,
  phone_num  INT,
  email      TEXT
);

CREATE TABLE AccountType (
  account_type_id INT PRIMARY KEY,
  account_type    TEXT
);

CREATE TABLE Accounts (
  account_id   SERIAL PRIMARY KEY,
  user_id      SERIAL REFERENCES Users (user_id),
  account_type INT, -- View AccountType to determine account type
  acct_amount  REAL,
  FOREIGN KEY (user_id) REFERENCES Users (user_id),
  FOREIGN KEY (account_type) REFERENCES AccountType (account_type_id)
);

CREATE TABLE TransactionType (
  transaction_type_id INT PRIMARY KEY,
  transaction_type    TEXT
);

CREATE TABLE Transactions (
  transaction_id      SERIAL,
  timestamp           TIMESTAMP WITH TIME ZONE,
  transaction_type    INT, -- View TransactionType to determine transaction type
  sender_id           SERIAL,
  sender_account_id   SERIAL,
  receiver_id         SERIAL,
  receiver_account_id SERIAL,
  transaction_amount  REAL,
  FOREIGN KEY (transaction_type) REFERENCES TransactionType (transaction_type_id),
  FOREIGN KEY (sender_id) REFERENCES Users (user_id),
  FOREIGN KEY (receiver_id) REFERENCES Users (user_id),
  FOREIGN KEY (sender_account_id) REFERENCES Accounts (account_id),
  FOREIGN KEY (receiver_account_id) REFERENCES Accounts (account_id)
);

