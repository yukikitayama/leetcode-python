"""
Binary search
Treat matrix like 1-d array
left 0, right: m*n - 1
Convert array index to matrix index
  e.g. m (row): 3, n (column): 4,
    if idx: 1, divide by n: 0, modulo by n: 1
    if idx: 5, divide by n: 1, modulo by n: 1
    if idx: 9, divide by n: 2, modulo by n: 1
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert 1d index to 2d index
            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            elif matrix[r][c] > target:
                right = mid - 1

        return False
