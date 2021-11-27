"""
- constructor
  - Initialize empty list
  - Initialize empty hashmap
- insert
  - Append val to the end of the list
  - Update hashmap with key the val and value the index
- remove
  - Use the hashmap to get the index of the removing val
  - Get the last element in the list
  - Insert the last element to the index
  - Update the hashmap with the last element index with the index
  - Pop the last element from the list
  - Delete the key the value from the hashmap
- getRandom
  - Generate random index
  - Use the index to access val
  - random.choice from the list
"""


import random


class RandomizedSet:
    def __init__(self):
        self.array = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        else:
            self.val_to_index[val] = len(self.array)
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        else:
            idx = self.val_to_index[val]
            last_val = self.array[-1]
            self.array[idx] = last_val
            self.val_to_index[last_val] = idx
            self.array.pop()
            del self.val_to_index[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.array)


obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())



