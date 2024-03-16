from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        left = 0
        right = len(nums) - 1

        while left < right:

            sum_ = nums[left] + nums[right]

            if sum_ < target:
                ans += 1
                left += 1
            else:
                right -= 1

        return ans

    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1

        return ans
