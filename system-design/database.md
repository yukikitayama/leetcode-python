# Database

## Caching

- Redis
- Memcached
- Hazelcast

## Blob storage

Blob means Binary Large OBject. Files like images and videos. Something which we will not query on but rather serve it as it is.

- Amazon S3

## Content Delivery Network (CDN)

Blobs are typically stored in Blob storage as primary source and multiple same files are stored in CDN, so that users
get the files from the closest server of the CDN to experience faster getting of the file. It means reducing latency.

## Text search engine

Allows us to do fuzzy search (e.g. airprot for airport)

- Elasticsearch
- Solr

## Time series database

Append only database, updated sequentially, used for metric tracking system.

- OpenTSDB
- InfluxDB

## Data warehouse

Dump all the available data and perform offline reporting and analytics.

- Hadoop

## RDBMS

- Need ACID
- Structured data

## Document database

- Need to specify data type
- Non structured
- Run queries for analysis

- MongoDB
- Couchbase

## Columnar database, column oriented database

- Non structured
- Ever increasing data
- finite queries
- If we have small number of queries but a large amount of data
- Huge scale of queries but less variety of queries, use columnar DB

- Cassandra
- HBase 

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