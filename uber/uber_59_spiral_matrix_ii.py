from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]

        # [print(row) for row in ans]

        count = 1

        for l in range((n + 1) // 2):

            # From left to right
            # As layer l gets higher, distance between left and right shrinks
            for i in range(l, n - l):
                ans[l][i] = count
                count += 1

            # From top to bottom
            for i in range(l + 1, n - l):
                ans[i][n - l - 1] = count
                count += 1

            # From right to left
            # i: n - l - 1, n - i - 1: n - (n - l - 1) - 1 = l
            for i in range(l + 1, n - l):
                ans[n - 1 - l][n - i - 1] = count
                count += 1

            # From bottom to top
            # n: 3, l: 0, n - l - 1: 3 - 1 = 2, i: (1,)
            for i in range(l + 1, n - l - 1):
                ans[n - i - 1][l] = count
                count += 1

        return ans


n = 3
n = 4
ans = Solution().generateMatrix(n)
[print(row) for row in ans]

