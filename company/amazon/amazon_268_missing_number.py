from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in nums_set:
                return number


nums = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(nums))
