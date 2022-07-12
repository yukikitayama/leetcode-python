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
- Huge individual and company (e.g. Uber) users


