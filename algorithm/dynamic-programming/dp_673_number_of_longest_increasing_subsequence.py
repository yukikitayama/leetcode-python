"""
dp[i]
  length of longest subsequence
  if current element is bigger than previous element
    +1 to the longest so far

Ans
  dp_length[i]
    longest length seen so far at i
  dp_count[i]
    count of longest length arrays ending at i
"""

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp_length = [1] * len(nums)
        dp_count = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):

                if nums[i] > nums[j]:

                    # Found longer
                    if dp_length[j] + 1 > dp_length[i]:
                        dp_length[i] = dp_length[j] + 1
                        dp_count[i] = dp_count[j]

                    # Update count
                    elif dp_length[j] + 1 == dp_length[i]:
                        dp_count[i] += dp_count[j]

            # print(dp_length)
            # print(dp_count)
            # print()

        # print(dp_length)
        # print(dp_count)

        max_length = max(dp_length)
        ans = 0
        for i in range(len(dp_count)):
            if dp_length[i] == max_length:
                ans += dp_count[i]

        return ans

    def findNumberOfLIS1(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        ans = 1
        max_length = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

                # Update
                if dp[i] == max_length:
                    ans += 1

                # Reset
                elif dp[i] > max_length:
                    max_length = dp[i]
                    ans = 1

        print(dp)

        return ans
