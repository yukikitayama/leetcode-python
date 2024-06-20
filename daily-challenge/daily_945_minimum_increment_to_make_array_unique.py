from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = [0] * (max(nums) + len(nums))
        for num in nums:
            count[num] += 1
        ans = 0
        for i in range(len(count) - 1):
            if count[i] > 1:
                move = count[i] - 1
                count[i + 1] += move
                ans += move
                count[i] = 1
        return ans

    def minIncrementForUnique1(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                new_num = nums[i - 1] + 1
                ans += (new_num - nums[i])
                nums[i] = new_num
        return ans