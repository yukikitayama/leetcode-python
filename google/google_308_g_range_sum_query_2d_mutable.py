from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        if self.rows == 0:
            return
        self.cols = len(matrix[0])
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        self.build_bit(matrix)

    def lsb(self, n: int) -> int:
        return n & (-n)

    def update_bit(self, r: int, c: int, val: int) -> None:
        i = r
        j = c
        while i <= self.rows:
            while j <= self.cols:
                self.bit[i][j] += val
                j += self.lsb(j)
            i += self.lsb(i)

    def query_bit(self, r: int, c: int) -> int:
        sum = 0
        i = r
        j = c
        while i > 0:
            while j > 0:
                sum += self.bit[i][j]
                j -= self.lsb(j)
            i -= self.lsb(i)
        return sum

    def build_bit(self, matrix: List[List[int]]) -> None:
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                val = matrix[i - 1][j - 1]
                self.update_bit(i, j, val)

    def update(self, row: int, col: int, val: int) -> None:
        old_val = self.sumRegion(row, col, row, col)
        row += 1
        col += 1
        diff = val - old_val
        self.update_bit(row, col, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        a = self.query_bit(row2, col2)
        b = self.query_bit(row1 - 1, col1 - 1)
        c = self.query_bit(row2, col1 - 1)
        d = self.query_bit(row1 - 1, col2)
        return (a + b) - (c + d)


"""
Tried to implement Python of Binary Indexed Tree Fenwick Tree
But it didn't work to the test case in this code and in LeetCode editor

https://leetcode.com/problems/range-sum-query-2d-mutable/solution/
https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75900/Python-2D-binary-indexed-tree

Time complexity

Space complexity
"""


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
sum_region_01 = [2, 1, 4, 3]
update = [3, 2, 2]
sum_region_02 = [2, 1, 4, 3]
# Output: [null, 8, null, 10]
num_matrix = NumMatrix(matrix)
print(num_matrix.sumRegion(*sum_region_01))
print(num_matrix.update(*update))
print(num_matrix.sumRegion(*sum_region_02))

