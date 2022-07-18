"""
- DP?
- prefix sum
"""


from typing import List
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])

        ps = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # - ps[i - 1][j - 1] for double count
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]

        # [print(row) for row in ps]
        # print()

        ans = 0

        for r1 in range(1, r + 1):
            for r2 in range(r1, r + 1):

                h = collections.defaultdict(int)
                h[0] = 1

                for col in range(1, c + 1):

                    # print(f'  col: {col}')

                    #
                    curr_sum = ps[r2][col] - ps[r1 - 1][col]
                    # print(f'    curr_sum: {curr_sum}')

                    ans += h[curr_sum - target]

                    h[curr_sum] += 1
                    # print(f'    h: {h}')

        return ans


if __name__ == '__main__':
    matrix = [[1, 0, -1, 0]]
    target = 0
    print(Solution().numSubmatrixSumTarget(matrix, target))


