from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c]

        # print('dp:')
        # [print(row) for row in self.dp]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = 0
        for r in range(row1, row2 + 1):
            answer += self.dp[r][col2 + 1] - self.dp[r][col1]

        return answer


matrix =[
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
query = [2, 1, 4, 3]
query = [1, 1, 2, 2]
query = [1, 2, 2, 4]
obj = NumMatrix(matrix)
print(obj.sumRegion(*query))
