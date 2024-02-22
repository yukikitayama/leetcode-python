"""

"""

from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            row = matrix[r]

            left_index = bisect.bisect_left(row, target)
            if left_index < len(row) and row[left_index] == target:
                return True

        return False