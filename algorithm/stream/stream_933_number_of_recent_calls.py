"""
[t - 3000, t]
queue
  S: O(N)
ping
  pop from left queue while queue head is less than (t - 3000)
  return length of queue
  T: O(N), amortized O(1)
"""

import collections


class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)