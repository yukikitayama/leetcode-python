class MyHashSet:
    def __init__(self):
        self.hash_key = 1999
        self.hashset = [[] for _ in range(self.hash_key)]

    def add(self, key: int) -> None:
        hashed_index = key % self.hash_key
        if not self.hashset[hashed_index]:
            self.hashset[hashed_index].append(key)
        else:
            for value in self.hashset[hashed_index]:
                if value == key:
                    return
            self.hashset[hashed_index].append(key)

    def remove(self, key: int) -> None:
        hashed_index = key % self.hash_key
        hashset = self.hashset[hashed_index]
        for i, value in enumerate(hashset):
            if value == key:
                self.hashset[hashed_index].pop(i)

    def contains(self, key: int) -> bool:
        hashed_index = key % self.hash_key
        hashset = self.hashset[hashed_index]
        for value in hashset:
            if value == key:
                return True
        return False


"""
Complexity
- Time
  - Let n be the number of possible values
  - Let k be the number of predefined buckets
  - Assumption is values are evenly distributed, so average size of bucket is n/k
  - Time is O(n/k) because in the worst case, it needs to scan the entire bucket.
"""


obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))

