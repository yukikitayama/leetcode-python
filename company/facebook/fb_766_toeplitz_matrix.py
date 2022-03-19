"""
- Two coordinates (row1, col1) and (row2, col2) are on the same diagonal
  as long as row1 - col1 == row2 - col2
"""


from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if not (r == 0 or c == 0 or matrix[r - 1][c - 1] == val):
                    return False
        return True


class Solution1:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Groups hashmap {row - col: a value in matrix}
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    matrix = [[1, 2], [2, 2]]
    print(Solution().isToeplitzMatrix(matrix))
