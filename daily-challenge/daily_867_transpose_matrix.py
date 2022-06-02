from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # matrix: (m, n) -> matrix: (n, m)
        ans = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]

        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    matrix = [[1, 2, 3], [4, 5, 6]]
    # [[1, 4], [2, 5], [3, 6]]
    print(Solution().transpose(matrix))
