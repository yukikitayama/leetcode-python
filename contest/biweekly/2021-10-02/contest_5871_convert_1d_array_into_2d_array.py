from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            return []

        ans = [[0] * n for _ in range(m)]

        row = 0

        for i, num in enumerate(original):
            col = i % n

            if i != 0 and col == 0:
                row += 1

            # print(f'i: {i}, row: {row}, col: {col}')

            ans[row][col] = original[i]

        return ans

        # for i in range(m * n):
        #     print(f'i: {i}, i // m: {i // m}, i % n: {i % n}')


"""
m: 3, n: 2, i: {0, 1, ..., 5}
i: 0, i: 1, col: 1
i: 1, i % m: 1 % 3 = 1, i % n: i % 2 = 1, i: 2, col: 2
i: 2, i % m: 1, i % n: 0, col: 0, i: 2, col: 0
"""

original = [1, 2, 3, 4]
m = 2
n = 2
# original = [1,2,3]
# m = 1
# n = 3
print(Solution().construct2DArray(original, m, n))
