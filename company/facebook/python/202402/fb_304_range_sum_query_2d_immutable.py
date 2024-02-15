"""
In init, we wanna pre-compute something
sumRegion wanna use the pre-computed result to quickly return sum

(top left, bottom right) - (top left, right) - (top left, down) + (top left, middle)

Prefix sum from top left to bottom right
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        # +1 to make it easy to compute prefix sum
        self.prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # minus at the end is subtracting the double-count by adding 2 prefix_sums
                self.prefix_sum[r + 1][c + 1] = matrix[r][c] + self.prefix_sum[r + 1][c] + self.prefix_sum[r][c + 1] - self.prefix_sum[r][c]

        # for row in self.prefix_sum:
        #     print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)