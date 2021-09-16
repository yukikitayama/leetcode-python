from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []

        rows = len(matrix)
        columns = len(matrix[0])
        up = 0
        left = 0
        right = columns - 1
        down = rows - 1

        while len(results) < rows * columns:

            # From left to right
            for col in range(left, right + 1):
                results.append(matrix[up][col])

            # From up to down
            for row in range(up + 1, down + 1):
                results.append(matrix[row][right])

            # From right to left
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    results.append(matrix[down][col])

            # From down to up
            if left != right:
                for row in range(down - 1, up, -1):
                    results.append(matrix[row][left])

            # Update boundary
            left += 1
            right -= 1
            up += 1
            down -= 1

        return results

"""
row: 3, col: 3
up: 0, left: 0, right: 2, down: 2,
range(left, right + 1): range(0, 3) = (0, 1, 2)
range(up + 1, down + 1): range(1, 3) = (1, 2)
range(right - 1, left - 1, -1): range(1, -1, -1) = (1, 0)
range(down - 1, up, -1): range(1, 0, -1) = (1,)
left: 1, right: 1, up: 1, down: 1


row: 3, col: 4

up: 0, left: 0, right: 3, down: 2,
range(left, right + 1): range(0, 4) = (0, 1, 2, 3)
range(up + 1, down + 1): range(1, 3) = (1, 2)
range(right - 1, left - 1, -1): range(2, -1, -1) = (2, 1, 0)
range(down - 1, up, -1): range(1, 0, -1) = (1,)
  matrix[1][0]

left: 1, right: 2, up: 1, down: 1
range(left, right + 1): range(1, 3) = (1, 2)
range(up + 1, down + 1): range(2, 2) = (), nothing happens for going down
if up != down: if 1 != 1: F, skip going left,
if left != right: if 1 != 2: T, range(down - 1, up, -1): range(0, 1, -1) = (), nothing happens for going up
  range is empty because stop is greater than start with negative
  also range will be empty if stop is less than start when step is positive


Time complexity
Let m be the number of rows and n be the number of columns in the matrix.
O(mn) because it traverses all the cells in the matrix

Space complexity
O(1) because we don't use extra data structure, and we don't include results because we are not supposed to
include the output array.
"""


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

