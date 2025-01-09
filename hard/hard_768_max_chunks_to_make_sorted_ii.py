from typing import List
import collections


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        counter = collections.Counter()
        ans = 0
        nonzero = 0

        for x, y in zip(arr, sorted(arr)):

            counter[x] += 1

            if counter[x] == 0:
                nonzero -= 1

            if counter[x] == 1:
                nonzero += 1

            counter[y] -= 1
            if counter[y] == -1:
                nonzero += 1
            if counter[y] == 0:
                nonzero -= 1

            if nonzero == 0:
                ans += 1

        return ans