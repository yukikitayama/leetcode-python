"""
Queue
Counter of value
consec
  append num
  update counter
  if queue size is bigger than k
    pop from left
    update counter
  if counter is k
    return true

T: O(1) for init and consec
S: O(k)
"""

import collections


class DataStream:

    def __init__(self, value: int, k: int):
        self.counter = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.counter += 1
        else:
            # Reset
            self.counter = 0
        return self.counter >= self.k


class DataStream1:

    def __init__(self, value: int, k: int):
        self.queue = collections.deque()
        self.counter = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.counter += 1

        if len(self.queue) > self.k:
            old_num = self.queue.popleft()
            if old_num == self.value:
                self.counter -= 1

        return True if self.counter == self.k else False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)