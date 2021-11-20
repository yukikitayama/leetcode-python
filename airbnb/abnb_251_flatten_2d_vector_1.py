from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.buffer = []
        for v in vec:
            self.buffer.extend(v)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.buffer[self.index]

    def hasNext(self) -> bool:
        if self.index < len(self.buffer) - 1:
            return True
        else:
            return False


"""
Complexity
- Time
  - Constructor is O(n)
  - next ad hasNext is O(1)
- Space
  - O(n) for buffer
  
Comment
- This is a bad implementation because
 - It does not utilized the existing vec list of list data structure
 - If the iterator only wants to access the first couple of elements, 
   taking O(n) in constructor wastes a lot of time.
"""


vec = [[1, 2], [3], [4]]
obj = Vector2D(vec)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())


