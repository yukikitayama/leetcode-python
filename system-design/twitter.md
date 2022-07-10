# Twitter

Twitter is a read heavy system, so that we need to either precompute the information or cache some of the information

We need the shortening URL service because, Twitter has the requirement for the length of text in tweets

When a user tweets, the tweet is stored in database, the posting tweet events triggers tweet processing service to 
create a cache of timeline, so that when a user requests a timeline, the data of the timeline comes from the cache, not
from the database, so it's fast. But the cache memory will be large, so only active users timeline is cached

Famous users have a large data, so it doesn't fit with cache

Search user interface can create a cache for frequently searched words, Redis.

## Functional requirement

- Post text, image, video, and links
- Share someone's tweets
- Follow someone
- Search

## Non functional requirement

- Read heavy
- Fast rendering
- Fast tweet
- It's okay to get notification about someone else's tweet a few seconds later, but the rendering of the content should
  be fast
- Scalable,because we have thousands of tweets that people post in every second, and Twitter is read heavy, so we have 
  even higher number of reads of the tweets that people post in every second.

## Categorize users

- Famous users
- Active users
  - Users who have accessed Twitter in the last few days.
- Live users
  - Users who are using Twitter right now. Subset of active users.
- Passive users
  - Users who have active accounts, but have not accessed Twitter in the last few days.
- Inactive users
  - Users who we assume to not exist anymore

## System breakdown

- Onboarding flow
- User-follow flow
- Tweet flow
- Search and analytics

## Onboarding flow

- Save user data in MySQL database, because the data is relational
- GET request with a user id is cached in Redis. If it doesn't exist in Redis, fetch the data from MySQL database.

## User-follow flow

### Graph service

- Add follow links
- Get users who a certain user is following
- Get users who are following a certain user
- Data is saved in MySQL, but assume the follow-links don't change frequently, so cache in Redis

### User live WebSocket service

- Keep open connections with all the **live users**
- Whenever an event occurs, such as a user who the live user is following tweets, send notification to the live user.

## Tweet flow

### Asset service

- Upload and display the text, images, videos or links

### URL shortener service

- Because tweets have a constraint of 280 characters, shorten a huge URLs.

### Tweet ingestion service

- Store the tweet texts and fetch them
- Use **Cassandra** as a permanent database, because it can have huge amount and can query.
- When a tweet is posted, the event is stored in **Kafka**

### Tweet processor

- When a user follows a huge list of users, querying all the tweets at runtime will be slow
- We cache the active user timeline in **Redis**

### Famous user tweets

- Famous user have lots of followers. Everytime a famous user tweets, we need to update the cache of all the followers
  timelines, but it's not good.
- So timeline cache only contains non-famous users tweets.
- A service gets a list of famous users who a certain user follows, and fetches their tweets.
- Update the cached tweets in Redis with timestamp.
- Next time to query, if the current timestamp is not that far from the cached timestamp, return  cached timeline

## Search and analytics

- Search results are saved in the database, but we can assume that other people search the tweets with the same search
  word, so the result is cached in Redis with some expiration.
- Spark keeps track of tranding keywords




