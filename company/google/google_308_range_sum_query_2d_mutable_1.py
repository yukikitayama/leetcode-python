from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.data = matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.data[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = 0
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                sum_region += self.data[r][c]
        return sum_region


"""
Time complexity
Let m be the row and n be the colum sizes of the matrix.
O(mn) for each query because nested for loops, and O(1) to update

Space complexity
If you don't count the matrix, O(1)
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

