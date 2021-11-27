"""
- Iterate each num in nums
- Add the current num to the max so far as long as mar so far plus current num is bigger than current num
- If not, reset it to the current num, because using sum of previous values does not beat current value
- as it iterates, keep track of the max so far
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = nums[0]
        max_subarray = nums[0]

        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(current_subarray, max_subarray)

        return max_subarray



nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))



