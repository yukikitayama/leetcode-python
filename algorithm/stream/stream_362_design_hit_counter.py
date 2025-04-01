"""
queue
hit append to queue
getHits
  popleft while given timestamp - 300 is bigger than or equal to queue head
  return size of queue

T:
  hit: O(1)
  getHits: O(N) at worst case, O(1) amortized time complexity
S: O(N)

If the number of hits per second is huger, queue takes a lot of memory, could crash


"""

import collections


class HitCounter1:

    def __init__(self):
        self.queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and (timestamp - 300) >= self.queue[0]:
            self.queue.popleft()

        return len(self.queue)


class HitCounter:

    def __init__(self):
        # [[timestamp, count], ...]
        self.queue = collections.deque()
        self.count = 0

    def hit(self, timestamp: int) -> None:
        if not self.queue or self.queue[0][0] != timestamp:
            self.queue.append([timestamp, 1])

        else:
            self.queue[0][1] += 1

        self.count += 1

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - 300 >= self.queue[0][0]:
            t, c = self.queue.popleft()
            self.count -= c

        return self.count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)