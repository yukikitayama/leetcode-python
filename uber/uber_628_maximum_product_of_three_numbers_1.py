"""
- 2 negatives okay
- 1 or 3 negatives not okay
"""


from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        p1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
        p2 = nums[n - 1] * nums[0] * nums[1]
        return max(p1, p2)


"""
Complexity
- Time is O(nlogn) to sort
- Space is O(n) to sort
"""


nums = [1,2,3,4]
nums = [-1,-2,-3]
print(Solution().maximumProduct(nums))


