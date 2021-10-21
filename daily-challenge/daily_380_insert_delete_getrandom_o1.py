"""
- constructor initializes item set
- insert() add it to set if not present
- remove() removes it from the set
- getRandom() random().randint(size of set)

Test
list: [51, 2, 10, 63, 57]
val: 10, last_element: list[-1] = 57, idx: dict[val] = dict[10] = 2,
  list[idx]: last_element = 57, dist[last_element]: idx = 2,
  list: [51, 2, 57, 63], dict: {51: 0, 2: 1, 63: 3, 57: 2}
"""


import random


class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.val_to_idx:
            last_val = self.vals[-1]
            idx = self.val_to_idx[val]
            self.vals[idx] = last_val
            self.val_to_idx[last_val] = idx
            self.vals.pop()
            del self.val_to_idx[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals)

