"""
- Ignore first row and first column to check
- Other cells need to check if their value is same as the value at row - 1, col - 1
- A given matrix is not always square
"""


from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r != 0 and c != 0 and matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
        return True


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    matrix = [[1, 2], [2, 2]]
    matrix = [[18],[66]]
    print(Solution().isToeplitzMatrix(matrix))
