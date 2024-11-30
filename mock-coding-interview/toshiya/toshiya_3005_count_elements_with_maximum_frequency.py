from typing import List
import collections


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        max_freq = max(counter.values())
        ans = 0
        for k, v in counter.items():
            if v == max_freq:
                ans += v

        return ans
