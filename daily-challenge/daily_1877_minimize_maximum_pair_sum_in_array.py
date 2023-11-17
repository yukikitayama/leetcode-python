"""
Max and min should be together
"""

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        ans = float("-inf")

        for i in range(len(nums) // 2):

            ans = max(ans, nums[i] + nums[-(i + 1)])

        return ans


if __name__ == "__main__":
    nums = [3, 5, 2, 3]
    nums = [3, 5, 4, 2, 4, 6]
    print(Solution().minPairSum(nums))
