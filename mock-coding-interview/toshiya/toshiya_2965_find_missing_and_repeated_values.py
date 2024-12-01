from typing import List
import collections


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        counter = collections.Counter()

        for i in range(1, (n * n) + 1):
            counter[i] = 0

        # grid = [[9,1,7],[8,9,2],[3,4,6]]
        for row in grid:
            # row: [9, 1, 7]
            for val in row:  # (9, 1, 7)
                counter[val] += 1

        ans = [0] * 2
        for k, v in counter.items():
            if v == 2:
                ans[0] = k
            elif v == 0:
                ans[1] = k
        return ans