"""
[1, 2]

[2, 1]

[1] -> [1, 3]

[3] -> [3, 4]

[4, 3]

[3, 4]

Queue?
How to move something in the middle of priority to recent?

Hashmap
  key: number
  value: value and priority

When hashmap exceeds the capacity, we cannot arbitrarily remove a key - we need to remove the least recently used one

Queue
  At left, least recently used
  At right, most recent
  When we get or put the existing key, we need to locate it in queue and move it to right most.

Sentinel node
"""

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)

        self.dic[key] = value

        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)