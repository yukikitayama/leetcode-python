"""
- Use left <= right binary search because of -1
- Mid starts from 0 and 10^4 / 2
  - compare with target and 2^31-1
"""


class ArrayReader:
    def get(self, index: int) -> int:
        pass


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:

        # Search boundary which contains target
        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        # Find the index of target
        while left <= right:
            mid = (left + right) // 2
            num = reader.get(mid)

            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            elif num < target:
                left = mid + 1

        return -1


class Solution1:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 10**4

        while left <= right:

            mid = (left + right) // 2

            curr = reader.get(mid)

            if curr == target:
                return mid
            elif curr == (2**31 - 1):
                right = mid - 1
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
