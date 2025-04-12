"""
Constructor
  hashmap
    if count is 1, append to queue

add
  update hashmap
  if count becomes 2
    scan queue and pop

ShowFirstUnique

"""

from typing import List
import collections


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.num_to_is_unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and not self.num_to_is_unique[self.queue[0]]:
            self.queue.popleft()
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value not in self.num_to_is_unique:
            self.num_to_is_unique[value] = True
            self.queue.append(value)
        else:
            self.num_to_is_unique[value] = False


class FirstUnique1:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque(nums)

    def showFirstUnique(self) -> int:
        for num in self.queue:
            if self.queue.count(num) == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)