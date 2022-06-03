"""
- 2 ways
  1. Pre compute prefix sum in constructor if given matrix can fit memory
  2. Compute in sumRegion if given matrix is too big

1. Cache row prefix sum, and in sumRegion, sum up each row sum diff
  - Time O(m)
2. Compute cumulative sum with respect to origin in 2d
  - Ans = biggest - top - left + top left
  - Time O(1)
"""


from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.cum_sum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # - top left so far because the part is doubled
                # ans = curr + top so far + left so far - top left so far
                # For cum_sum r+1 and c+1 is curr, for matrix, r and c is curr
                self.cum_sum[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.cum_sum[r + 1][c]
                    + self.cum_sum[r][c + 1]
                    - self.cum_sum[r][c]
                )

        # [print(row) for row in self.cum_sum]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # all - top - left + top left
        return self.cum_sum[row2 + 1][col2 + 1] \
               - self.cum_sum[row1][col2 + 1] \
               - self.cum_sum[row2 + 1][col1] \
               + self.cum_sum[row1][col1]


class NumMatrix1:
    def __init__(self, matrix: List[List[int]]):
        self.cum_sum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.cum_sum[r][c + 1] = self.cum_sum[r][c] + matrix[r][c]

        # [print(row) for row in self.cum_sum]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2 + 1):
            ans += self.cum_sum[r][col2 + 1] - self.cum_sum[r][col1]
        return ans


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))
    # 8
    print(obj.sumRegion(1, 1, 2, 2))
    # 11
    print(obj.sumRegion(1, 2, 2, 4))
    # 12


