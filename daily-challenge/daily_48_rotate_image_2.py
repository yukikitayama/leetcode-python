from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # n % 2 to go to the middle row if n is odd
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):

                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]

                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]

                matrix[j][n - 1 - i] = matrix[i][j]

                matrix[i][j] = tmp


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:

        def transpose(mat):
            for r in range(len(mat)):
                for c in range(r + 1, len(mat)):
                    mat[c][r], mat[r][c] = mat[r][c], mat[c][r]

        def reflect(mat):
            for r in range(len(mat)):
                for c in range(len(mat[0]) // 2):
                    mat[r][-c - 1], mat[r][c] = mat[r][c], mat[r][-c - 1]

        transpose(matrix)

        # for row in matrix:
        #     print(row)
        # print()

        reflect(matrix)

        # for row in matrix:
        #     print(row)
        # print()


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().rotate(matrix))
