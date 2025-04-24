"""
[_, _, _, X, X]
n: 5
right: 3
5 - 3 = 2 + 1
"""

from typing import List
import collections


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        distinct = len(set(nums))
        counter = collections.Counter()
        right = 0

        for left in range(len(nums)):

            if left > 0:
                counter[nums[left - 1]] -= 1
                if counter[nums[left - 1]] == 0:
                    del counter[nums[left - 1]]

            while right < len(nums) and len(counter) < distinct:
                counter[nums[right]] += 1
                right += 1

            # Here, right is 1 step further

            if len(counter) == distinct:
                # +1 for one step further
                ans += len(nums) - right + 1

        return ans