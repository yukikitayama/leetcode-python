# Video Conference (Video Chat) Application

## Example

- Zoom
- WebEx
- Whatsapp or Facebook video call
- Google Meet

## Functional requirement

- 1 to 1 calls
- Group calls
- Audio / Video / Screen share
- Record video call

## Non functional requirement

- Platform is super fast, if lagged, user experience is bad
- High availability
- Data loss is okay. A couple of video frames missing is okay, because a user won't even realize it

## TCP

- Transport layer protocol
- A data lossless protocol
- Tries to the best of its ability to make sure that there is no data loss happening between a client and a server
- If a client cannot obtain an acknowledgement for a particular packet (data) from a server, tries to replay that. 
- Packets ordering guaranteed
- Chats are handled by TCP

### Congestion control

- If too much congestion on the network, it delays sending a certain package to make sure the network will not be 
  overwhelmed by a lot of packets

## UDP

- Lossy protocol
- There could potentially be some of the data loss
- But it will guarantee that it will be faster
- Packets ordering not guaranteed
- Video transfer is handled by UDP

## WebRTC

- Web real time communication




