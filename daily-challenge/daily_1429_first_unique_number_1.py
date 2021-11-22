"""
Idea
- In constructor, make Counter
- Make an array containing values which have count 1
  - Hashmap with key value and value index to the array
- showFirstUnique()
  - if the array is empty, return -1
  - otherwise return the first element in the array
- add()
  - If the value exist in the Counter, increment
    - If the count was 1, pop the value from the array
      - Use the second hashmap to find the value in the array using the index
  - If the value does not exist in the Counter,
    - append the value to the array, and add it to the Counter

- There's no remove operation, so the unique number, if added for the second time, won't be unique again
- No need to count, because it only requires seen once or not, so instead use boolean

"""


from typing import List
import collections


class FirstUnique:
    def __init__(self, nums: List[int]):
        self._queue = collections.deque(nums)
        self._is_unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self._queue and not self._is_unique[self._queue[0]]:
            self._queue.popleft()
        if self._queue:
            return self._queue[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue.append(value)
        else:
            self._is_unique[value] = False





