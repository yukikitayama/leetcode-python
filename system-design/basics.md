# System Design Basics

## High Level Design

Design should be future proof, meaning the system should be non-restrictive and pluggable for an additional requirement
at a later stage and avoid need to redesign the entire existing system.

## Low Level Design

- Individual components
- Optimizations within the components
- Clean, modularized, future-proof code
  - **Future-proof** means that when we need to add a new feature in the future, the current design should not restrict 
    it. 

## Monolithic architecture

- Monolith is typically good for a small team, a few services
- Many people say that microservices architecture is better, but the monolith has the following benefits
  - Microservices have a higher latency typically for API communications, which are slower than function calls in a 
    monolith.
  - Each network call among microservices can fail by network failure.
  - Microservices need an extra logging service to aggregate logs from each microservice to monitor system

## Microservices

- Microservices are typically good for large organizations, and hundreds or thousands of services.
- Typically used in interviews

## Inter-service communication

- Hybrid, mandatory process is synchronous, everything else is asynchronous
- Message queues to call asynchronous process to be fault-tolerant
  - If one of the systems which depends on message queues is down, the messages will remain in the queue until the
    service is back up, so the data won't get lost
  - Message queue software examples; Kafka, Rabbit MQ, Active MQ

## WebSockets

- Establish a persistent connection, typically first introduced by HTTP request
- Bidirectional communication so server can send data to client too
- High frequency communication is possible, meaning **high throughput**
- Disadvantage is that we will have a high cost of hardware. If there are many users, we need to maintain persistent 
  connection with each user.
- Example is chat application

## Consistent hashing

## Caching

- Cashing is only helpful when we can predict that the same data will be request again in the near future.

## Rate limit

- Prevent bots from doing random things on our websites
  - Scraping
  - Stealing
  - Spammingb  
- Prevent DOS and DDOS attack
- Prevent spams
- Leaky bucket
- Fixed window
- Sliding window