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
        right = 1

        # Find right boundary
        if reader.get(left) == target:
            return left

        while reader.get(right) < target:
            left = right
            right *= 2

        # Normal binary search
        while left <= right:
            mid = (left + right) // 2

            if reader.get(mid) == target:
                return mid

            elif reader.get(mid) < target:
                left = mid + 1

            elif reader.get(mid) > target:
                right = mid - 1

        return -1

    def search1(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 10 ** 4 - 1
        while left <= right:
            mid = (left + right) // 2

            if reader.get(mid) == target:
                return mid

            elif reader.get(mid) == 2 ** 31 - 1:
                right = mid - 1

            elif reader.get(mid) < target:
                left = mid + 1

            elif reader.get(mid) > target:
                right = mid - 1

        return -1
