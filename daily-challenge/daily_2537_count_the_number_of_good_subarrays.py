"""
Counter hashmap
"""

from typing import List
import collections


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        ans = 0
        right = -1
        pair = 0

        for left in range(len(nums)):

            while pair < k and right + 1 < len(nums):
                right += 1
                pair += counter[nums[right]]
                counter[nums[right]] += 1

            if pair >= k:
                # n: 4, right: 2, left: 0, subarrays: [(0 to 0), (0 to 1)]
                ans += len(nums) - right

            counter[nums[left]] -= 1
            pair -= counter[nums[left]]

        return ans