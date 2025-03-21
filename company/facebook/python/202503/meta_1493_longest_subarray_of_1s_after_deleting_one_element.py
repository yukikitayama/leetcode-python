"""
if a window contains one zero, length is number of ones
if a window contains more than one zero, shrink window
if a window doesn't contain zero, length is number of ones - 1
"""

from typing import List
import collections


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counter = collections.Counter()
        left = 0
        ans = 0
        for right in range(len(nums)):

            counter[nums[right]] += 1

            while counter[0] > 1:
                counter[nums[left]] -= 1
                left += 1

            # print(left, right, counter)

            if counter[0] > 0:
                ans = max(counter[1], ans)
            else:
                ans = max(counter[1] - 1, ans)

        return ans