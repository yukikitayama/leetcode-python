# Caching

**Cache** is a storage for a high speed data access by fetching previously computed data. If we think we will query
again the same data, we will cache it. If we don't find anything in the cache, we will compute the data, save it to 
the cache, and return it to the users. We want to store a commonly or recently used data that doesn't change frequently,
and we believe a user will fetch again in the near future.

## Speed

Caches are stored in RAM. It avoids the lookup time by database

## Benefit

- Reduce latency
- Reduce resource utilization
- Avoid fetching a computationally heavy data over and over
- Save network and service calls
- Cache tends to respond faster than the databases

## Avoid cases

- When the data needs to be consistent
- Read once but many writes
- Data fetching doesn't repeat

## Cache size

The larger the cache storage is, the longer it will take to fetch data from the cache. Use cache eviction strategy.

- Time to live, TTL, to make the data in cache expire. After expiration, data fetch requests don't go to cache, but go
  to database.
- Size based to keep the cache size small and respond fast.
  - First In First OUT is simple but not used in practice
  - Least frequently used, LFU, to delete the data that were not used frequently.
  - Least recently used, LRU, to delete the data that wasn't used recently.
  - Least frequently recently used, LFRU, a combination of LFU and LRU, used in practice.

## Metrics

- Size
  - Bigger cache, performance reduced, cost increases
- Latency
  - Not good if database is faster than fetching from cache
- Cache hit rate
  - Number of fetching data from cache / Number of total data requests
  - Adding cache in system actually adds a step, because before checking the database, we need to check cache first, so
    if cache doesn't have the relevant data, requests always take an unnecessary step
  - Cache miss rate, inverse of cache hit rate