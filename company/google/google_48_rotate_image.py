from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # n // 2 + n % 2 gives us the max index to go to the hald of array regardless of even or odd
        # print(f'n // 2: {n // 2}')
        # print(f'n % 2: {n % 2}')

        # By using n - 1 - i, and n - 1 - j, going from outer to inner, because i and j increment
        # But increment until the half of index

        for i in range(n // 2 + n % 2):
            # print(f'i: {i}')
            for j in range(n // 2):
                # print(f'j: {j}')
                # print(f'n - 1 - j: {n - 1 - j}')
                # n - 1 - j goes from end to half index, because n is fixed but j increments
                # i increments from 0 to half index
                tmp = matrix[n - 1 - j][i]
                # print(f'tmp: {tmp}')
                # print(f'n - 1 - i: {n - 1 - i}, n - j - 1: {n - j - 1}')
                # print(f'matrix[n - 1 - i][n - 1 - j]: {matrix[n - 1 - i][n - 1 - j]}')
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

            # print()

        # [print(row) for row in matrix]


"""
Time complexity
Let m be the number of cells, O(m) because iterate all the cells

Space complexity
O(1) because no extra data structures used
"""


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(Solution().rotate(matrix))
