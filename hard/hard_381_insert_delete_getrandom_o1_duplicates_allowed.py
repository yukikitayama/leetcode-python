"""
Hashmap
"""

import collections
import random


class RandomizedCollection:

    def __init__(self):
        self.array = []
        self.val_to_idx = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        self.val_to_idx[val].add(len(self.array))
        self.array.append(val)
        return len(self.val_to_idx[val]) == 1

    def remove(self, val: int) -> bool:
        # If empty
        if not self.val_to_idx[val]:
            return False

        idx_remove = self.val_to_idx[val].pop()
        val_last = self.array[-1]
        idx_last = len(self.array) - 1

        # Overwriting acts like deleting
        self.array[idx_remove] = val_last

        # Add new index of last value to hashmap
        self.val_to_idx[val_last].add(idx_remove)

        # Remove previous index of last value from hashmap
        self.val_to_idx[val_last].discard(idx_last)

        # Remove previous index of last value from array
        self.array.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.array)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()