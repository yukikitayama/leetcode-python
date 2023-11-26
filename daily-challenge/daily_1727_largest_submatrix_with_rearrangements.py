from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]

            curr_row = matrix[i][:]
            curr_row.sort(reverse=True)

            for j in range(n):
                ans = max(ans, curr_row[j] * (j + 1))

        return ans


if __name__ == "__main__":
    matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]]
    print(Solution().largestSubmatrix(matrix))
