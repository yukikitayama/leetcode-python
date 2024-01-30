"""
dp(x1, y1, x2, y2)
  base
    x1 == x2 and y1 == y2 and cell == target, return 1, otherwise return 0
  recurrence
    count + dp(row + 1, col) + dp(row - 1, col) + dp(row, col + 1) + dp(row, col - 1)


dp(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
"""

from typing import List
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        r = len(matrix)
        c = len(matrix[0])

        # Compute 2D prefix sum
        # +1 for the first element prefix sum
        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # Prefix sum = up + left - left upper + current
                # left upper is subtracted because (up + left) double-counts that section
                # -1 for matrix because ps is bigger than matrix by size 1
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]

        # for row in ps:
        #     print(row)

        ans = 0

        # ???
        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):
                h = collections.defaultdict(int)
                h[0] = 1

                for col in range(1, c + 1):
                    # current 1D prefix sum
                    curr_sum = ps[r2][col] - ps[r1 - 1][col]

                    # add subarrays which sum up to (curr_sum - target)
                    ans += h[curr_sum - target]

                    # save current prefix sum
                    h[curr_sum] += 1

        return ans


if __name__ == "__main__":
    matrix = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    target = 0
    # 4

    print(Solution().numSubmatrixSumTarget(matrix, target))


