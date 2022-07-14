# Google Maps System DesignTokyo, Japan

## Functional requirement

- Users can see route, distance, and time between two points
- Pluggable (Avoid changing the entire architecture)
  - Traffic information
  - Weather
  - Accident
  - Construction

## Non functional requirement

- High availability (This should not go down)
- Good accuracy
- Not too slow to provide results to users (A few seconds is okay, no need to be milliseconds fast)
- Scalable because of huge individual and company (e.g. Uber) users

## Cache

- Cache the shortest path information between various points to avoid running graph algorithm again and again to 
  recalculate the shortest path

## Shortest path

- Assume it's a function of distance, estimated time of arrival, and average speed between two points
- Assume average speed is a function of traffic condition and weather condition.
- When these change, average speed change. When the speed change, shortest path will change, so run the algorithm to 
  recalculate.
- But because we cannot run algorithm every time attributes change, we set threshold. When attribute changes by more 
  than X%, run algorithm to recalculate.

## System architecture





