from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []

        # Only the first is lower - 1 for edge case
        prev = lower - 1

        for i in range(len(nums) + 1):

            if i < len(nums):
                curr = nums[i]
            # Only the last one is upper + 1 for edge case
            else:
                curr = upper + 1

            if prev + 1 <= curr - 1:
                answer = self.formatRange(prev + 1, curr - 1)
                result.append(answer)

            prev = curr

        return result

    def formatRange(self, lower, upper):
        if lower == upper:
            return str(lower)
        else:
            return f'{str(lower)}->{str(upper)}'


"""
Time complexity
Let n be the length of nums, O(n) because for loop to nums

Space complexity
O(1) because the result list is the output, not counted for the purpose of space complexity, 
but we have a few variables to save data.
"""


nums = [0,1,3,50,75]
lower = 0
upper = 99
print(Solution().findMissingRanges(nums, lower, upper))
