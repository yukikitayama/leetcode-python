"""
Algorithm
- Assume I can modify the matrix in place
- Iterate each row from 1 to the end of row in the matrix
  - If column index is 0, current row[i] = current row[i] + min(previous row[i], previous row[i + 1])
  - If column index is at the last column in the matrix, current row[i] = current row[i] + min(previous row[i - 1],
    previous row[i])
  - Else, current row[i] = current row[i] + min(previous row[i - 1], previous row[i], previous row[i + 1])
- return min(last row of the matrix)

Complexity
- Time: O(nm) by n row and m col
- Space: O(1) because of inplace modification
"""


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):

                if col == 0:
                    matrix[row][col] = matrix[row][col] + min(matrix[row - 1][col], matrix[row - 1][col + 1])

                elif col == len(matrix[0]) - 1:
                    matrix[row][col] = matrix[row][col] + min(matrix[row - 1][col - 1], matrix[row - 1][col])

                else:
                    matrix[row][col] = matrix[row][col] + min(
                        matrix[row - 1][col - 1],
                        matrix[row - 1][col],
                        matrix[row - 1][col + 1]
                    )

        return min(matrix[-1])


matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]
matrix = [[-48]]
print(Solution().minFallingPathSum(matrix))





