"""
Hashamp
  k: num, v: count
"""


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def lower_bound(low, high, target):
            while low <= high:
                mid = low + ((high - low) // 2)
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        nums.sort()
        ans = 0
        for i in range(len(nums)):
            low = lower_bound(i + 1, len(nums) - 1, lower - nums[i])
            high = lower_bound(i + 1, len(nums) - 1, upper - nums[i] + 1)
            ans += high - low

        return ans

    def countFairPairs1(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    ans += 1
        return ans