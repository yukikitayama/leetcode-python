from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        # Left and right pointers
        l = 0
        r = 1

        current_max = nums[0]
        current_min = nums[0]

        # Answer is initialized with 1 because length 1 nums can give us 1 by [8] => 8 - 8 = 0 <= limit
        answer = 1

        while l <= r < len(nums):
            # With a new right pointer, update current max and min
            current_max = max(current_max, nums[r])
            current_min = min(current_min, nums[r])

            if current_max - current_min <= limit:
                answer = max(answer, r - l + 1)

            # Move left pointer so update current max and min as well
            else:
                if nums[l] == current_max:
                    # r + 1 because python array slicer of end is exclusive
                    new_subarray = nums[l + 1: r + 1]
                    current_max = max(new_subarray)
                if nums[l] == current_min:
                    new_subarray = nums[l + 1: r + 1]
                    current_min = min(new_subarray)

                l += 1

            # Move right pointer
            r += 1

        return answer


"""
Time complexity
Let n be the length of nums. O(n) for while loop

Space complexity
O(1)
"""


nums = [8,2,4,7]
limit = 4
nums = [10,1,2,4,7,2]
limit = 5
print(Solution().longestSubarray(nums, limit))
