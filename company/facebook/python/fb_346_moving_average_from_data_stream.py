"""
init
  initialize queue
  set size to attribute
  initialize total to be 0
  initialize count to be 0

next method
  Queue to append val from right
    increment total
    increment count if queue < size
  If queue size > given size, popleft
    decrement total by popped value

  T: O(1)
  S: O(N)
    N is size
"""

import collections


class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.size = size
        self.total = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        self.count += 1

        if self.count > self.size:
            popped = self.queue.popleft()
            self.total -= popped
            self.count -= 1

        average = self.total / self.count

        return average

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)