"""
"""


from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # dp row and column are one length bigger than matrix
        # so dp row + 1 corresponds to row in matrix, and
        # dp col + 1 corresponds to col in matrix
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r + 1][c + 1] = (
                    self.dp[r + 1][c]
                    + self.dp[r][c + 1]
                    + matrix[r][c]
                    - self.dp[r][c]
                )

        # print('Matrix')
        # [print(row) for row in matrix]
        # print('Cumulative sum from the origin')
        # [print(row) for row in self.dp]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row2 + 1][col1]
            - self.dp[row1][col2 + 1]
            + self.dp[row1][col1]
        )


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # 8
print(obj.sumRegion(1, 1, 2, 2))  # 11
print(obj.sumRegion(1, 2, 2, 4))  # 12
