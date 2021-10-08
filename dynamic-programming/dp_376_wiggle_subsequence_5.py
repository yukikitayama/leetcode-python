from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        pos = 1
        neg = 1

        for i in range(1, len(nums)):

            diff = nums[i] - nums[i - 1]

            if diff > 0:
                pos = 1 + neg
            elif diff < 0:
                neg = 1 + pos

        return max(pos, neg)


nums = [1,7,4,9,2,5]
# nums = [1,17,5,10,13,15,10,5,16,8]
# nums = [1,2,3,4,5,6,7,8,9]
print(Solution().wiggleMaxLength(nums))
