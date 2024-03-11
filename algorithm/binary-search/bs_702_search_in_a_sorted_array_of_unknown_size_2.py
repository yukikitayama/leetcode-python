"""
mid starts from the mid between 0 and 2**31 - 1
  if returned value < target
    search to right
  if returned value > target
    search to left
  if equal,
    return mid
  if returned value is 2**31 - 1
    out of bound,
    so search to left
"""


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
   def get(self, index: int) -> int:
       pass


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 2 ** 31

        while left <= right:

            mid = (left + right) // 2

            returned_val = reader.get(mid)

            if returned_val == target:
                return mid
            elif returned_val < target:
                left = mid + 1
            elif returned_val > target:
                right = mid - 1

        return -1
