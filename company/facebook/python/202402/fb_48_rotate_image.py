"""
Start from left to right
  Swap anti clockwise 4 times
  After one row finishes, go down one row, but column shrink

"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # Bottom left
                tmp = matrix[n - 1 - j][i]
                # Bottom left = Bottom right
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # Bottom right = Top right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # Top right = Top left
                matrix[j][n - 1 - i] = matrix[i][j]
                # Top left
                matrix[i][j] = tmp

    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflect:
        for row in matrix:
            row.reverse()
