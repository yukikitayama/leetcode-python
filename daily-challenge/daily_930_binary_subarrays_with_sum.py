from typing import List
import collections


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_to_count = collections.Counter()
        prefix_sum = 0
        ans = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            if prefix_sum == goal:
                ans += 1

            if prefix_sum - goal in prefix_sum_to_count:
                ans += prefix_sum_to_count[prefix_sum - goal]

            prefix_sum_to_count[prefix_sum] += 1

        return ans

    def numSubarraysWithSum1(self, nums: List[int], goal: int) -> int:
        ans = 0

        for left in range(len(nums)):
            for right in range(left, len(nums)):
                if sum(nums[left:right + 1]) == goal:
                    ans += 1

        return ans
