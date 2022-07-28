# Chat Application

## Example

- Facebook messenger
- Whatsapp

## Functional requirement

- One-on-one chat
- Group chat
- Upload files
- Indicate read or received status of a message
- Indicate the last seen each user was seen

## Non functional requirement

- Low latency to feel real-time chat
- High availability
- No lag
- Scalable

## Race condition

- WebSocket handler for a user keeps **polling** messages from the server every few minutes, so any messages which missed previously can be
  seen now by the user.

## Local caching

- Save the messages when a user is offline and made in a **local database of the device**, and send them once the device
  gets connected to the internet

## Group message

- Put a group message into Kafka topic and save a message ID and group ID in topic
- Group message handler consumes the topic, gets a list of users in a group
- Finds all the WebSocket handlers which each connects to each user
- And ask them to send a group message

## File delivery

- Save a file in the database such as S3
- A service issues a file ID
- file ID is sent to another user
- The user fetches the file by the file ID from the database.
- It could happen that the same files are shared by many users. Before uploading files to S3, get a hash of a file,
  and search if the hash exist in database. If exists, won't upload but return the file ID and the receiving user uses
  the ID to get the file from the database.

## Analytics

- Find who is favorite of a certain user by frequency of checking a message window
- Find topics which users are interested in by checking words in a message

