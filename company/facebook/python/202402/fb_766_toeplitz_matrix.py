"""
Iterate every cell
  when row != 0 and col != 0
    if matrix[row][col] != matrix[row - 1][col - 1]
      return False
return True

T: O(NM)
S: O(1)
"""

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row != 0 and col != 0:
                    if matrix[row][col] != matrix[row - 1][col - 1]:
                        return False
        return True