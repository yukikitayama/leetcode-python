"""
If we have only one set to save integersm
  insert and remove are T: O(1)
  but getRandom will be T: O(N) because it takes O(N) to convert set to list, and from the list, we can pick

  Before getRandom, we need to have list of unique integers in advance
    how to delete one element from list by T: O(N)
      left end and right end can be T: O(1) if deque

  2 stacks?

Array
  Store integers
Hashset
  k: val
  v: index

eg
  [1]
    {1: 0}
  [1, 2]
    {1: 0, 2: 1}
  remove 1 -> get 1's index 0 from hashmap -> pop last element -> put the last element to 0th position
"""

import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        index = len(self.nums)
        self.val_to_index[val] = index
        self.nums.append(val)

        # print(f"insert: {val}, {self.nums}")

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]

        self.nums[index] = self.nums[-1]
        self.val_to_index[self.nums[-1]] = index
        self.nums.pop()

        del self.val_to_index[val]

        # print(f"remove: {val}, {self.nums}, {self.val_to_index}")

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()