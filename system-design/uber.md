# Uber

## Functional requirement

- See cabs around you
- ETA and price
- Able to book a cab
- Tracking location

## Non functional requirement

- Low latency
- High availability
- High consistency
- Scalable

## Segment

- Discretize a continuous map into multiple rectangular segments
- Identify which segment a customer or a diver belongs to
- If a segment has too many drivers, cut the segment into smaller segments
- If a segment has a few drivers, merge the segments into a bigger segment to contain more drivers.

## WebSocket

- All the active drivers have open connections by WebSocket for us to get locations and send notifications about trips

## Mode

- Classify customers and drivers to priorities, such as average or premium
- If a premium customer requests, give them the best driver.




