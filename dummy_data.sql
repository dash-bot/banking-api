/*
 * dummy_data.sql
 *
 * Created on: 2018-01-13
 *
 * Load sample data for banking API.
 */


-- Load sample user data
INSERT INTO users (user_id, first_name, last_name, phone_num, email)
VALUES (342450, 'AJ', 'Po-Deziel', 2506665423, 'ajpd@etc.com'),
  (940128, 'Charlie', 'Friend', 2509024878, 'cf@etc.com'),
  (591044, 'Paul', 'Sajna', 2506803455, 'ps@etc.com'),
  (789243, 'Rhys', 'Lawson', 2504531237, 'rl@etc.com'),
  (298473, 'Shae', 'Brown', 2507678889, 'sb@etc.com');

-- Load available account types
INSERT INTO account_type (account_type_id, account_type) VALUES (1, 'chequing'), (2, 'savings');

-- Load sample account data
INSERT INTO accounts (account_id, user_id, account_type, acct_amount)
VALUES (987234, 342450, 1, 1076.46),
  (542024, 342450, 2, 1298.30),
  (413267, 940128, 1, 1536.65),
  (123704, 940128, 2, 922.43),
  (219873, 591044, 1, 1388.76),
  (618393, 591044, 2, 1205.32),
  (120439, 789243, 1, 2013.45),
  (122983, 789243, 2, 467.98),
  (982734, 298473, 1, 710.03),
  (276384, 298473, 2, 2151.87);

-- Load sample available transaction types
INSERT INTO transaction_type (transaction_type_id, transaction_type) VALUES (1, 'account_transfer'), (2, 'etransfer');

