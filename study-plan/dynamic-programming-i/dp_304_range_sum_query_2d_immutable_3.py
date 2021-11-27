"""
Example
[3, 0, 1, 4, 2],
[5, 6, 3, 2, 1],
[1, 2, 0, 1, 5],
[4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]

Cumulative sum
[3, 3, 4, 8, 10]
[5, 11, 14, 16, 17]
[1, 3, 3, 4, 9]
[4, 5, 5, 6, 13]
[1, 1, 4, 4, 9]

Red area top left: (row1: 2, col1: 1) and down right: (row2: 4, col2: 3)
- sum is 8
- answer from cumulative sum is
  - For each row
    - cumulative row[col2] - cumulative[col1 - 1]
- But the above will be index out of bound when col1 is 0 and col2 is also 0
- Append a column to left side of the cumulative sum with 0s
  - cumulative row[col2 + 1] - cumulative[col1]

Example
- row1: 3, col1: 0, row2: 4, col2: 1
  - for each row in cumulative sum matrix
    - cumulative row[2] - cumulative row[0]
      = cumulative row[col2 + 1] - cumulative row[col1]

Cumulative sum
[0, 3, 3, 4, 8, 10]
[0, 5, 11, 14, 16, 17]
[0, 1, 3, 3, 4, 9]
[0, 4, 5, 5, 6, 13]
[0, 1, 1, 4, 4, 9]


Algorithm
- Get cumulative sum for each row
- Sum region for (row1, col1) and (row2, col2) is
  - Iterate each row in cumulative sum rows
    - cumulative sum row[col2] - cumulative[col1]

Complexity
- Time:
  - init: O(nm) by m row, n col
  - sumRegion: O(m)
- Space: O(mn)
"""


from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.cumsum = [[0] * (self.n + 1) for _ in range(self.m)]
        for i in range(len(self.cumsum)):
            for j in range(1, len(self.cumsum[0])):
                self.cumsum[i][j] = self.cumsum[i][j - 1] + matrix[i][j - 1]

        # [print(row) for row in self.cumsum]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            row_sum = self.cumsum[i][col2 + 1] - self.cumsum[i][col1]
            ans += row_sum
        return ans


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # 8
print(obj.sumRegion(1, 1, 2, 2))  # 11
print(obj.sumRegion(1, 2, 2, 4))  # 12
