"""
init
  T: O(1)
  S: O(1)
next
  T: O(1)
"""

import collections


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.circular_queue = [0] * size
        self.head = 0
        self.sum_ = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        # Next position to the current head is a tail to be removed
        tail = (self.head + 1) % self.size

        self.sum_ = self.sum_ + val - self.circular_queue[tail]

        # Store current value to the tail position in the circular queue
        self.head = (self.head + 1) % self.size
        self.circular_queue[self.head] = val

        return self.sum_ / min(self.size, self.count)


class MovingAverage1:

    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.sum_ = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum_ += val
        if len(self.queue) > self.size:
            num = self.queue.popleft()
            self.sum_ -= num
        return self.sum_ / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)