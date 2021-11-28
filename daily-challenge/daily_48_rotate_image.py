"""
"""

# TEST_CASE = [[1,2,3], [4,5,6], [7,8,9]]
TEST_CASE = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]


class Solution:
    def rotate(self, matrix):
        print(f'Original matrix')
        for row in matrix:
            print(row)
        print()
        self.transpose(matrix)
        print(f'Transposed matrix')
        for row in matrix:
            print(row)
        print()
        self.reflect(matrix)
        print(f'Reflected matrix')
        for row in matrix:
            print(row)
        print()

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                print(f'i: {i}, j: {j}')
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                print(f'i: {i}, j: {j}, (-j-1): {-j-1}')
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


def main():

    sol = Solution()
    sol.rotate(matrix=TEST_CASE)


if __name__ == '__main__':
    main()
