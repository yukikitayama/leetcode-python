# Notification Sevice

## Functional requirement

- Send notifications
- Pluggable
  - SMS
  - Email
  - Within app notification
- Prioritization
  - High priority: password reset
  - Low priority: promotional message

## Non functional requirement

- High availability
- Easy enough to add more clients

## Rate limiter

- How many times in a certain time, a user is allowed to send messages
- How many times in a certain time, we can send messages to a user

## Bulk notification

- Query users from database
