# Facebook System Design

## Functional requirement

- Able to post text, image, video
- Able to like, comment, and share of a post
- Add friend as non-directional
- See timeline of yourself
- See others' profile and posts
- Log and track every activity that a user does

## Non functional requirement

- Read heavy
- Fast rendering of someone's post and profile and fast posting 
- Lag is okay, but low latency. It means that posts can be available to other users after a few ten seconds, but the 
  response of rendering and posting should be quick
- Find a particular access pattern to posts
- Global
- Most of the users access from mobile devices

## Users

- Famous
- Active
  - e.g. Users who accessed Facebook in the last 3 days.
  - We optimize the pages are rendered fast
- Live
  - Notification
- Passive
  - No cache
- Inactive

## Database

- Use MySQL 
  - To store user information 
  - To store friendship information

## Caching

- Use Redis
- User details
- Friends
- User type (Active, Famous, Passive, ...)
- Relevance tags to share or notify amount the same interest people
  - We wanna show relevant information to users
- Last access time
- Data of the only last few days











