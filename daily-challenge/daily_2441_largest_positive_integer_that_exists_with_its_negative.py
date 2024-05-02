from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1

        for i in range(len(nums)):

            if -nums[i] in seen:
                ans = max(ans, abs(nums[i]))

            seen.add(nums[i])

        return ans

    def findMaxK1(self, nums: List[int]) -> int:
        ans = -1

        negatives = set([num for num in nums if num < 0])

        for i in range(len(nums)):

            if -nums[i] in negatives:
                ans = max(ans, nums[i])

        return ans