"""
"""


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = current_jump_end = farthest = 0

        for i in range(len(nums) - 1):
            # In the current jump, check how far we can reach
            farthest = max(farthest, i + nums[i])

            # If the current jump ends by i comes to the current jump end index,
            # we say that we had jump and check the next index when the next jump reaches
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps


nums = [2,3,1,1,4]
print(Solution().jump(nums))
