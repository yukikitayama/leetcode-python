from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):

            if i % 10 == nums[i]:
                return i

        return -1


nums = [0, 1, 2]
nums = [4,3,2,1]
nums = [1,2,3,4,5,6,7,8,9,0]
nums = [2,1,3,5,2]
print(Solution().smallestEqual(nums))

