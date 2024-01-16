"""
binary search for each row, find min index to insert 1
  if min index < len(row)
    1 exist
  else:
    1 doesn't exist
return minimum of min indices
"""

from typing import List
import bisect


class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        pass

    def dimensions(self) -> List[int]:
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        n, m = binaryMatrix.dimensions()
        smallest_index = m

        for row in range(n):

            left = 0
            right = m - 1

            while left < right:

                # Lower-middle
                mid = (left + right) // 2

                cell = binaryMatrix.get(row, mid)

                if cell == 0:
                    # +1 because mid was 0, so it can't be 1 cell
                    left = mid + 1
                elif cell == 1:
                    # No -1 to mid because mid could be the first 1
                    right = mid

            if binaryMatrix.get(row, left):
                smallest_index = min(smallest_index, left)

        return -1 if smallest_index == m else smallest_index


if __name__ == "__main__":
    matrix = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]

    for row in matrix:
        print(bisect.bisect_left(row, 1))