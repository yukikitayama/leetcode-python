"""
if current is bigger than prev
  increment curr length
  prev = curr
else:
  reset length to 1
  prev = curr
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = float("-inf")
        length = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] > prev:
                length += 1
                ans = max(ans, length)

            else:
                length = 1

            prev = nums[i]

        return ans
