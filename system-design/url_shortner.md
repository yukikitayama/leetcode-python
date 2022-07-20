# URL Shortner Service

## Example

- TinyURL
- Bitly

## Functional requirement

- Given a long URL, return a short URL
- When a user hits the short URL, redirect the user to the long URL.

## Non functional requirement

- Low latency
- High availability

## Clarification

- How many **unique** URLs do we need to shorten in a certain interval, such as per second?
- What duration of time do we need to support, such as `X` years?
- What characters are allowed?

## Compute the length of short URL

If `X` number of requests for shortening URL comes per second, and if we need to support `Y` years,

`X * 60 seconds * 60 minutes * 24 hours * 365 days * Y years = Z`

If we use a set of characters `a-z, A-Z, 0-9`, we have `26 + 26 + 10 = 62` characters available.

To make length `1` short URLs, we have `62` combinations. To make length `2` short URLs, we have `62^2` combinations.

Why? Because for each character in the short URLs, we have `62` options to choose.

To generalize, to make length `n` short URLs, we have `62^n` combinations.

Because we need to support `Z` number of unique short URLs, `62^n > Z`, `n > log_62 (Z)`

## Analytics

- Every time we get a request to generate short URLs, get attributes like platform, devices, IP addresses to know 
  clients
- Save the information into a Kafka
