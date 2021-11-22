"""
- Complexity
  - K is the length of nums, n is the total number of operations
  - Constructor is O(k)
  - add() is O(1) for if statament, add, remove
  - showFirstUnique() is O(1) for if statement hashset check and getting first element in the set
"""


from typing import List
import collections


class FirstUnique:
    def __init__(self, nums: List[int]):
        self._queue = collections.OrderedDict()
        self._is_unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self._queue:
            return next(iter(self._queue))
        return -1

    def add(self, value: int) -> None:
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue[value] = None
        # Second time appearing
        elif self._is_unique[value]:
            self._is_unique[value] = False
            # pop() method of dict class
            # pop(key) retrieves the value at key and also removes the key and value from dict object
            # so it can remove item from the middle
            self._queue.pop(value)





