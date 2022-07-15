# Booking System

## Example

- Airbnb
- Booking.com

## Functional requirement

- Hotel owners
  - Onboard
  - Update property information
  - See how bookings are
- Users to stay
  - Search
  - Book
  - Check the booked information
- Analytics

## Non functional requirement

- Low latency
- High availability
- High consistency
- Scale

## System design

- Hotel owners can upload images of properties, and the images are stored in CDN for fast rendering, so MySQL database 
  only stores the URLs of the images
- To support search, use Elastic Search to enable a fuzzy search, because users will make typos

## Booking

## Database

- Divide data center by geography to reduce latency
- Create multiple data centers within a regional to create replica to increase availability
  - When something goes wrong, change the DNS of users coming to another data center with replicated from the primary
    data center.


