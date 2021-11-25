"""
- Start: 8:55
- End: 8:59

- Kadane's algorithm
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = nums[0]
        curr = ans

        for i in range(1, len(nums)):

            # putting nums[i] in max() resets the sum so far
            curr = max(nums[i], curr + nums[i])
            ans = max(ans, curr)

        return ans


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
print(Solution().maxSubArray(nums))


