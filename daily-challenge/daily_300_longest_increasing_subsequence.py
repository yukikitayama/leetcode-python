from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        # i is index at the end
        for i in range(1, len(nums)):

            # j is indices before i
            for j in range(i):

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
print(Solution().lengthOfLIS(nums))
