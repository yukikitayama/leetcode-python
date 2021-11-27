"""
- First trial, TLE
- Let n be the length of incoming keys
- inc() takes O(1)
- dec() takes O(1)
- getMaxKey() takes O(n)
- getMinKey() takes O(n)
"""


import collections


class AllOne:

    def __init__(self):
        self.key_to_count = collections.defaultdict(int)

    def inc(self, key: str) -> None:
        self.key_to_count[key] += 1

    def dec(self, key: str) -> None:
        self.key_to_count[key] -= 1

        if self.key_to_count[key] == 0:
            del self.key_to_count[key]

    def getMaxKey(self) -> str:
        max_count = float('-inf')
        max_key = ''
        for key, count in self.key_to_count.items():
            if count > max_count:
                max_key = key
                max_count = count
        return max_key

    def getMinKey(self) -> str:
        min_count = float('inf')
        min_key = ''
        for key, count in self.key_to_count.items():
            if count < min_count:
                min_key = key
                min_count = count
        return min_key


obj = AllOne()
obj.inc('hello')
obj.inc('hello')
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc('leet')
print(obj.getMaxKey())
print(obj.getMinKey())

# ["AllOne","getMaxKey","getMinKey"]
# [[],[],[]]


