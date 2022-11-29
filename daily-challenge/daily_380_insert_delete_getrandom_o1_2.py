import random


class RandomizedSet:
    def __init__(self):
        self.value_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        idx = len(self.values)
        self.values.append(val)
        self.value_to_index[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False

        # Exchange in array
        idx_delete = self.value_to_index[val]
        idx_last = len(self.values) - 1
        val_last = self.values[idx_last]
        self.values[idx_delete], self.values[idx_last] = self.values[idx_last], self.values[idx_delete]

        # Update hashmap
        self.value_to_index[val_last] = idx_delete
        del self.value_to_index[val]

        # Update array
        self.values.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
