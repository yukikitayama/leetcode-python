"""
mat = [
[1,2,3],
[4,5,6],
[7,8,9]
]

range sum of mat[0][0], mat[0][1], mat[1][0], mat[1][1]
= row sum + col sum - double counted part + the bottom right corner
= (1 + 2) + (1 + 4) - (1) + (5)
= 3 + 5 - 1 + 5
= 12

range sum of whole mat
= 21 + 27 - 12 + 9
= 48 - 3
= 45

rangeSum
[0, 0, 0, 0]
[0, 1, 3, 6]
[0, 5, 12, 21]
[0, 12, 27, 45]
- 12 at rangeSum[2][2] is 1 + 2 + 4 + 5 in mat

rangeSum[i + 1][j + 1] corresponds to mat[i][j]
so rangeSum[i][j] is previous cell in mat

answer
- mat[0][0], k: 1, range sum of mat[0][0], mat[0][1], mat[1][0], mat[1][1]
- 45 - 12 - 6 + 1 = 45 - 18 + 1 = 46 - 18 = 28
"""


from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # Get the sum from the top left cell to the down right cell
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                rangeSum[i + 1][j + 1] = (
                    rangeSum[i + 1][j]
                    + rangeSum[i][j + 1]
                    - rangeSum[i][j]
                    + mat[i][j]
                )

        # [print(row) for row in rangeSum]

        # Get the sum depending on the boundary of k
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Top left cell
                r1 = max(0, i - k)
                c1 = max(0, j - k)

                # Down right cell
                r2 = min(m, i + k + 1)
                c2 = min(n, j + k + 1)

                # print(f'Top left: ({r1}, {c1}), down right: ({r2}, {c2})')

                answer[i][j] = (
                    rangeSum[r2][c2]
                    - rangeSum[r2][c1]
                    - rangeSum[r1][c2]
                    + rangeSum[r1][c1]
                )

        # [print(row) for row in answer]

        return answer


mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(Solution().matrixBlockSum(mat, k))

