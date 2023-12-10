from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[None] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                ans[c][r] = matrix[r][c]

        return ans


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(Solution().transpose(matrix))
