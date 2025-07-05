from typing import List
import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        counter = collections.Counter(arr)
        for k, v in counter.items():
            if k == v:
                ans = max(ans, k)
        return ans