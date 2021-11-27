from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        # print('mat')
        # [print(row) for row in mat]

        m = len(mat)
        n = len(mat[0])

        # n + 1? m + 1?
        # + 1 gives us the extra first row and first column
        # rangeSum calculation becomes easier because it does not have to
        # care about the first row and first column edge case in summation
        # so initialized with 0
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                # Careful because rangeSum uses rangeSum AND mat
                # both length of indices are different, because rangeSum has the extra one index
                rangeSum[i + 1][j + 1] = (
                    rangeSum[i + 1][j]
                    + rangeSum[i][j + 1]
                    - rangeSum[i][j]
                    + mat[i][j]
                )

        # print('rangeSum')
        # [print(row) for row in rangeSum]

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                row_min = max(0, i - k)
                col_min = max(0, j - k)
                # + 1 because rangeSum has extra 1
                row_max = min(m, i + k + 1)
                col_max = min(n, j + k + 1)
                # m: 3, n: 3, k: 1, i: 0, j: 0,
                # row_min: 0, col_min: 0, row_max: min(3, 2) = 2, col_max: min(3, 2) = 2

                # m: 3, n: 3, k: 2, i: 0, j: 0
                # row_min: 0, col_min: 0, row_max: min(3, 3) = 3, col_max: 3
                # i: 0, j: 1
                # row_min: 0, col_min: 0, row_max: min(3, 3) = 3, col_max: min(3, 4) = 3
                ans[i][j] = (
                    rangeSum[row_max][col_max]
                    - rangeSum[row_max][col_min]
                    - rangeSum[row_min][col_max]
                    + rangeSum[row_min][col_min]
                )

        return ans


mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
k = 2
print(Solution().matrixBlockSum(mat, k))
