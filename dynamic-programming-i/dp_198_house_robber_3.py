from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        rob_next_next = 0
        rob_next = nums[n - 1]

        for i in range(n - 2, -1, -1):
            current = max(rob_next, rob_next_next + nums[i])
            rob_next_next = rob_next
            rob_next = current

        # Return rob_next, instead of current.
        # When nums is [0], for loop won't run, and current is not assigned yet,
        # but rob_next contains the answer, and also, in the for loop, at the end
        # current and rob_next have the same values
        return rob_next


"""
Dynamic programming space optimzed

Time complexity
Let n be the length of nums. O(n) to iterate for loop

Space complexity
O(1) because we got rid of dynamic programming table.
"""


nums = [1, 2, 3, 1]
nums = [2,7,9,3,1]
# nums = [0]
print(Solution().rob(nums))

