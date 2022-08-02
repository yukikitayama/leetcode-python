# Database

## MySQL database

- When data can be described as a table
- When you want ACID

### ACID

ACID means Atomic, Consistent, Isolated and Durable

- Atomic means that all transactions are guaranteed to be either successful completely or fail completely.
- Consistent means that database is consistent before and after the transaction, so we feel it's correct.
- Isolated means that all transactions take place in isolation, meaning one transaction will not affect another ongoing
  transaction. It allows us to make parallel concurrent transactions without making inconsistency
- Durability means that once a transaction is complete, the changes are written to disk.

## MongoDB

- When you have a vast variety of attributes
- Need to run a vast variety of queries
- The attributes are different for each data

## Cassandra

- When you have an ever-increasing amount of data and a huge scale of queries
- Less variety in queries so that most queries include a common partition key in the where clause
- It needs to replicate data but with a different partition key

Deletes are not handled very efficiently

Ever-increasing data