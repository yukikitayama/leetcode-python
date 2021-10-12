"""
-

"""


from typing import List


class Solution:
    def countSquare(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        ans = 0

        for row in range(m):
            for col in range(n):

                if matrix[row][col] == 1:

                    if row == 0 or col == 0:
                        ans += 1

                    else:
                        curr_cell = matrix[row][col] + min(
                            matrix[row - 1][col],
                            matrix[row][col - 1],
                            matrix[row - 1][col - 1]
                        )
                        ans += curr_cell
                        matrix[row][col] = curr_cell

        return ans


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
print(Solution().countSquare(matrix))





