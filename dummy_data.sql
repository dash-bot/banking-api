/*
 * dummy_data.sql
 *
 * Created on: 2018-01-13
 *
 * Load sample data for banking API.
 */


-- Load sample user data
INSERT INTO Users (pwd, first_name, last_name, phone_num, email)
VALUES ('abc123', 'AJ', 'Po-Deziel', 1234567890, 'ajpd@etc.com'),
  ('abc123', 'Charlie', 'Friend', 9876543210, 'cf@etc.com'),
  ('abc123', 'Shae', 'Brown', 4567890123, 'sb@etc.com');


-- Load available account types
INSERT INTO AccountType (account_type_id, account_type) VALUES (1, 'Chequing'), (2, 'Savings');


-- Load sample account data
INSERT INTO Accounts (user_id, account_type, acct_amount)
VALUES (1, 1, 100.00), (1, 2, 1000.00), (2, 1, 500.00), (2, 2, 2500.00), (3, 1, 700.00), (3, 2, 1200.00);


-- Load sample available transaction types
INSERT INTO TransactionType (transaction_type_id, transaction_type) VALUES (1, 'IntraTransfer'), (2, 'ETransfer');


SET TIME ZONE LOCAL;


-- Load sample transaction data
INSERT INTO Transactions (timestamp, transaction_type, sender_id, sender_account_id, receiver_id, receiver_account_id, transaction_amount)
VALUES ('2018-01-14'::TIMESTAMP, 2, 1, 2, 3, 1, 500.00);

