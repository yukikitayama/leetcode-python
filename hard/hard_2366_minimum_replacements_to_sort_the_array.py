from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums) - 2, -1, -1):

            # Sorted
            if nums[i] <= nums[i + 1]:
                continue

            # Count how many elements are made
            # If divisible
            # nums[i]: 6, nums[i + 1]: 3, 6 -> [3, 3]
            if nums[i] % nums[i + 1] == 0:
                num_elements = nums[i] // nums[i + 1]

            # If not divisible
            # nums[i]: 7, nums[i + 1]: 3, 7 // 3: 2, 7 -> [2, 2, 3]
            else:
                num_elements = nums[i] // nums[i + 1] + 1

            # Compute number of operations: breaking nums[i] into n elements requires n - 1 steps
            ans += num_elements - 1

            # Update current element for the next comparison
            # nums[i]: 10, nums[i + 1]: 3, 10 // 3 + 1 = 4, 10 -> [2, 2, 3, 3], 10 // 4 = 2
            # average value is the maximum smallest value at leftmost
            nums[i] //= num_elements

        return ans