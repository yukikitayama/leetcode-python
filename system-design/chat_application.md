# Chat Application

## Example

- Facebook messenger
- Whatsapp

## Functional requirement

- One-to-one chat
- Group chat
- Upload files
- Read receipt
- Last seen 

## Non functional requirement

- Low latency to feel real-time chat
- High availability
- No lag

## Race condition

- WebSocket handler for a user keeps pulling messages from the server, so any messages which missed previously can be
  seen now by the user.

## When device is offline

- Save the messages when a user is offline and made in a local database of the device, and send them once the device
  gets connected to the internet

## Group message

- Put a group message into Kafka topic
- Group message handler consumes the topic, gets a list of users in a group
- Finds all the WebSocket handlers which each connects to each user
- And ask them to send a group message

## File upload

- Save a file in the database
- A service issues a file ID
- file ID is sent to another user
- The user fetches the file by the file ID from the database.

## Analytics

- Find who is favorite of a certain user by frequency of checking a message window
- Find topics which users are interested in by checking words in a message

