from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        result = 0

        for r in range(rows):
            for c in range(cols):

                if matrix[r][c] == 1:

                    # Only for the top row and most left column
                    # it does not have the futher top left cells to form a bigger square
                    # so only count on the cell itself
                    if r == 0 or c == 0:
                        result += 1

                    else:
                        # min(upper left, left, upper)
                        cell_val = min(matrix[r - 1][c - 1], matrix[r][c - 1], matrix[r - 1][c]) + matrix[r][c]
                        result += cell_val
                        # Update matrix itself to memoize
                        matrix[r][c] = cell_val

        return result


"""
[0, 1, 1, 1],
[1, 1, 2, 2],
[0, 1, 2, 3]

Time complexity
Let m be the number of rows and n be the number columns in the matrix
O(nm) because it iterates each cell in the matrix

Space complexity
O(i) because it updates input matrix in place.
"""


matrix = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]
print(Solution().countSquares(matrix))
