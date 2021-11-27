from typing import List
import collections


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.is_unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and not self.is_unique[self.queue[0]]:
            self.queue.popleft()
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.queue.append(value)
        else:
            self.is_unique[value] = False


"""
Complexity
- Time
  - Constructor O(n)
  - showFirstUnique O(n)
  - add O(1)
- Space
  - O(n) for queue and counter
  
Result
- TLE
"""


nums = [2, 3, 5]
obj = FirstUnique(nums)
print(obj.showFirstUnique())
obj.add(5)
print(obj.showFirstUnique())
obj.add(2)
print(obj.showFirstUnique())
obj.add(3)
print(obj.showFirstUnique())



