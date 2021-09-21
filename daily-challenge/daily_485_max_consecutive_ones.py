from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = max_count = 0

        for num in nums:

            if num == 1:
                curr_count += 1

            # Encounter 0
            else:
                # Save max counter before reset current counter
                max_count = max(max_count, curr_count)

                curr_count = 0

        # At above, we count end with 1, in that case, max_count is not updated yet
        # so instead of returning max_count, we do max(max_count, curr_count) again
        return max(max_count, curr_count)


"""
Time complexity
Let n be the length of nums. O(n) to do one pass

Space complexity
O(1) because it only uses constant data
"""

# nums = [1, 1, 0, 1, 1, 1]
nums = [1,0,1,1,0,1]
print(Solution().findMaxConsecutiveOnes(nums))
