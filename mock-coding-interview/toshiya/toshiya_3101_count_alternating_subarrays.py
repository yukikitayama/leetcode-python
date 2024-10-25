"""
Dynamic programming
  No

Two pointers
nums = [1,0,1,0]
exp: 10
 1 + (1 + 1) + (1 + 1 + 1) + (1 + 1 + 1 +) = 1 + 2 + 3 + 4 = 10
"""

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        """T: O(N)"""

        ans = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] == nums[right - 1]:
                left = right

            ans += (right - left + 1)

        return ans

    def countAlternatingSubarrays1(self, nums: List[int]) -> int:
        """T: O(N^2)"""
        ans = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    ans += 1

                else:
                    if nums[j] != nums[j - 1]:
                        ans += 1
                    else:
                        break

        return ans