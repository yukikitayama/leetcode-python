from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        # print(f'matrix:')
        # [print(row) for row in matrix]

        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # - self.dp[r][c] because it's double counted in summation dp
                # r: 0, c: 1
                # dp[1][2] = dp[1][1] + dp[0][2] + matrix[0][1] - dp[0][1]
                self.dp[r + 1][c + 1] = (
                    self.dp[r + 1][c]  # row wise cumsum
                    + self.dp[r][c + 1]  # column wise cumsum
                    + matrix[r][c]  # additional number for cumsum from matrix
                    - self.dp[r][c]  # double counted region to be subtracted
                )

        # print('dp array, cumulative sum from the origin')
        # [print(row) for row in self.dp]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # print(f'row1: {row1}, col1: {col1}, row2: {row2}, col2: {col2}')

        sum_region = (
            self.dp[row2 + 1][col2 + 1]  # Cumulative sum from origin which covers too much. +1 because of dp array
            - self.dp[row1][col2 + 1]  # Top right rectangle to be subtracted
            - self.dp[row2 + 1][col1]  # Down left rectangle to be subtracted
            + self.dp[row1][col1]  # Top left rectangle subtracted too much so add back in
        )
        return sum_region


"""
Time complexity
- Initialization takes O(mn) by letting m be the number of rows and n be the number of columns
- query takes O(1)

Space complexity
- DP array take O(mn)
"""


matrix =[
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
# query = [2, 1, 4, 3]  # 8
# query = [1, 1, 2, 2]  # 11
query = [1, 2, 2, 4]  # 12
obj = NumMatrix(matrix)
print(obj.sumRegion(*query))
