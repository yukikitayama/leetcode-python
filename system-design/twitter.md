# Twitter

Twitter is a read heavy system, so that we need to either precompute the information or cache some of the information

We need the shortening URL service because, Twitter has the requirement for the length of text in tweets

When a user tweets, the tweet is stored in database, the posting tweet events triggers tweet processing service to 
create a cache of timeline, so that when a user requests a timeline, the data of the timeline comes from the cache, not
from the database, so it's fast. But the cache memory will be large, so only active users timeline is cached

Famous users have a large data, so it doesn't fit with cache

Search user interface can create a cache for frequently searched words, Redis.
