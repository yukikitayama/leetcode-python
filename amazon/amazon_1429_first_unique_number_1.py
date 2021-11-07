from typing import List
import collections


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = collections.deque(nums)
        self.counter = collections.Counter(nums)

    def showFirstUnique(self) -> int:
        for num in self.queue:
            if self.counter[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counter[value] += 1


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



