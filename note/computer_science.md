# Computer Science

## Chunked Transfer Encoding

- Data stream is divided into chunks.
- Each chunk is preceded by its size in bytes.
- [Wiki](https://en.wikipedia.org/wiki/Chunked_transfer_encoding)

## Run Length Encoding

- e.g. `nums: [1, 1, 1, 2, 2, 2, 2, 2] -> encoded: [[1, 3], [2, 5]]`, three 1s followed by five 2s.
- [Run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding)

## Defang link

- `Defaning link` is a way to prevent a user from inadvertently clicking a malicious link
  - e.g. `http -> hxxp` in URL, `1.1.1.1 -> 1[.]1[.]1[.]1` in IP address.
  - [Email Security – Defanging URLs](https://www.ibm.com/docs/en/sqsp/32.0?topic=SSBRUQ_32.0.0/com.ibm.resilient.doc/install/resilient_install_defangURLs.htm)
  - `Defang`: make (something) harmless or ineffectual.

## Iterator Pattern

- [Iterator Pattern](https://www.geeksforgeeks.org/iterator-pattern/)
- [284. Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)