from typing import List
import bisect


class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        return 0

    def dimensions(self) -> List[int]:
        return [0, 0]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        smallest_index = cols

        for row in range(rows):
            lo = 0
            hi = cols - 1

            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid

            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)

        return -1 if smallest_index == cols else smallest_index


mat = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]
