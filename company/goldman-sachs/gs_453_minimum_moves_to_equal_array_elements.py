from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 0, -1):
            # 0 and i are incremented same amount, so the difference between 0 and each index
            # the sum will be the total moves
            count += nums[i] - nums[0]
        return count


"""
- Time is O(nlogn) for sorting
- Space is O(n) for sorting
"""


nums = [1,2,3]
# nums = [1,1,1]
print(Solution().minMoves(nums))
