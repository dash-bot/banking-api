# Dash: Banking API

#### For more detailed information, check out Dash on [Devpost](https://devpost.com/software/dash-5wq83e)!
#### Created at nwHacks 2018


## What is this API used for?
This is one of three microservices that make up Dash, and provides it with a basic bank structure connected to a **PostgreSQL database on AWS RDS**. It also contains sample data of customers and sample transactions so that it can be queried against.

The service is then used, for example, with [conversation-server](https://github.com/dash-bot/conversation-server) for use with **Microsoft Cognitive Services' LUIS** when customers query it for information regarding their accounts.
