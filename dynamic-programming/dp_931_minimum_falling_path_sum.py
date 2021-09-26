from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):

                # Left edge
                if col == 0:
                    matrix[row][col] = min(
                        matrix[row][col] + matrix[row - 1][col],
                        matrix[row][col] + matrix[row - 1][col + 1]
                    )

                # Right edge
                elif col == len(matrix[0]) - 1:
                    matrix[row][col] = min(
                        matrix[row][col] + matrix[row - 1][col - 1],
                        matrix[row][col] + matrix[row - 1][col]
                    )

                # Other every element in the middle
                else:
                    matrix[row][col] = min(
                        matrix[row][col] + matrix[row - 1][col - 1],
                        matrix[row][col] + matrix[row - 1][col],
                        matrix[row][col] + matrix[row - 1][col + 1]
                    )

        return min(matrix[len(matrix) - 1])



matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]
matrix = [[-48]]
print(Solution().minFallingPathSum(matrix))

