"""
constructor
  empty n length array
  pointer initialized to 0
insert
  insert value at idKey in array
  empty array as return
  while pointer is not none
    append current to return array
    increment pointer
  return
"""

from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.array = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey - 1] = value
        res = []
        while self.pointer < len(self.array) and self.array[self.pointer]:
            res.append(self.array[self.pointer])
            self.pointer += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)