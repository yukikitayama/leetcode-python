"""

"""

import random


class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.val_to_idx:
            self.val_to_idx[val] = len(self.vals)
            self.vals.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_idx:
            last_val = self.vals[-1]

            # Get both indices
            remove_index = self.val_to_idx[val]
            last_val_index = self.val_to_idx[last_val]

            # Move the removed val to the end
            # and move the original last val to somewhere before the last
            self.vals[last_val_index] = val
            self.vals[remove_index] = last_val

            # Update hashmap
            self.val_to_idx[val] = last_val_index
            self.val_to_idx[last_val] = remove_index

            # Delete
            self.vals.pop()
            del self.val_to_idx[val]

            return True

        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.vals)


