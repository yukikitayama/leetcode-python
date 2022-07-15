# Netflix System Design

## Functional requirement

- Upload video
- Search video
- Play video
- Support multiple devices
  - Devices
  - Video format
  - Dimension of video
  - Bandwidth

## Non functional requirement

- No buffering, or minimize buffering
- Low latency
- High availability
- Increase user session time

## Content delivery network (CDN)

- After processing the video into many smaller chunks to avoid lag at user side, upload the processed video files to CDN
- Service will identify which video a user wants to watch and where the user comes from, and provide the best CDN video
  files to achieve low latency.

## Consumers

### Client

- Device type with video playing functionality
- Laptop
- Mobile phone

### Users

- Viewer of the content
- Human

### Production houses

- Users who upload videos

## Video transfer

- Cut a video smaller chunks
- While users watching the first chunks, download the second chunks
- When a certain quality of video is not available, request a lower quality of video

