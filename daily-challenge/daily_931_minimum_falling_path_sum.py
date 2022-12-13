from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):

                if c == 0:
                    matrix[r][c] += min(matrix[r - 1][c], matrix[r - 1][c + 1])

                elif c == len(matrix[0]) - 1:
                    matrix[r][c] += min(matrix[r - 1][c - 1], matrix[r - 1][c])

                else:
                    matrix[r][c] += min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r - 1][c + 1])

        return min(matrix[len(matrix) - 1])


if __name__ == '__main__':
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(Solution().minFallingPathSum(matrix))
