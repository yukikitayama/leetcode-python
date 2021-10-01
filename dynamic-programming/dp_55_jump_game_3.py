"""
- dp[i] represents a boolean of whether you can reach num in nums at the index of i
- Base case dp[0] is True because we start at the first index
- Get num at i
- Update max_furthest to be i + num
- go to the next i
- update max_furthest
- iterate until len(nums) - 1
- return if max_furthest is equal to or greater than len(nums) - 1
"""


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Maximum index we can jump to
        max_far = 0

        for i in range(len(nums)):
            num = nums[i]
            current_far = i + num

            # If i is equal to or smaller than max_far, it means we can reach the current index
            # by the jumps we have seen so far
            if i <= max_far:
                max_far = max(max_far, current_far)
            # Otherwise we cannot reach further indices, so no need to iterate
            else:
                break

            # print(f'i: {i}, nums[i]: {nums[i]}, max_far: {max_far}')

        # If max_far has not exceeded the last index in nums, we failed to reach so return False
        return True if max_far >= len(nums) - 1 else False


nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
print(Solution().canJump(nums))

