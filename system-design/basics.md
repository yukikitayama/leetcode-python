# System Design Basics

## Who needs to know

- Software engineer
- Product manager
- Technical program manager

## High Level Design

High level design includes

- Overall architecture
- Systems and services
- Interaction between systems
- Databases
- Example

This design is expected to

- Satisfy functional requirements and non-functional requirements
- Highly scalable
- Non-restrictive and modular to be futuristic

### Functional requirements

- What features does the system/service have?
- What does a user experience through the service?

### Non functional requirements

- How does the service need to scale?
- What's the latency expectation?
- Is consistency required?

## Approach to high level system design

1. Clarify functional and non functional requirements
2. Propose a design by defining components, databases, interactions among them
3. Clarify trade-offs, e.g. SQL or NoSQL database?
4. Clarify multiple design choices exist and which one is the best for a specific system
5. Consider limitations and what's missing from the designed system.

## Low Level Design

Low level design means

- Discuss the detail of an individual component of all the components in the system (**subsystem**). 
- Discuss the optimization of the individual component
- Describe examples

Low level design expects us to

- Satisfy functional and non functional requirement
- Have a good structure of set of codes
- Have a working and clean code
- Have non-restrictive modular codes to be futuristic

## Approach to low level system design

1. Describe functional and non functional requirements
2. Make a set of codes
   1. Define interfaces
   2. Make class diagrams
   3. Define data model
3. Keep the quality in the code
   1. Code is working
   2. Code is modular
   3. Code is testable

## Monolithic architecture

- Monolith is typically good for a small team, a few services
- Problems of monolithic architecture are
  - Bounded by a single technology
  - Easy to break things because it's hard to know the boundaries of subsystems.
  - Difficult scale when traffic spikes
  - Deployment of a single subsystem is to need to deploy the entire system.
- Many people say that microservices architecture is better, but the monolith has the following benefits
  - Microservices have a higher latency typically for API communications, which are slower than function calls in a 
    monolith.
  - Each network call among microservices can fail by network failure.
  - Microservices need an extra logging service to aggregate logs from each microservice to monitor system

## Microservices

- Benefits of microservices are
  - Tech stack freedom, e.g. Frameworks, Databases.
  - Separation of concerns
  - Easy for engineers to understand the code base
  - Deployment can be frequent and faster
  - Scaling of each subsystem can be independent
- Problems of microservices are
  - Higher latency because of API calls for each subsystem to talk to each other
  - Exposed to network failure because subsystem needs to talk to each other
  - Logs are stored in each subsystem, so we need to develop logging service to collect and aggregate from all the subsystems
  - Additional access and security management of each subsystem
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