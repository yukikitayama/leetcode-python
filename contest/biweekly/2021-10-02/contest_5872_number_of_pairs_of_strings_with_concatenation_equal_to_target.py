from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> str:

        ans = 0

        for i in range(len(nums)):
            for j in range(len(nums)):

                if i != j:
                    concatenated = nums[i] + nums[j]
                    if concatenated == target:
                        ans += 1

        return ans


nums = ["777", "7", "77", "77"]
target = "7777"
print(Solution().numOfPairs(nums, target))
