from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        def two_sum_smaller(nums, start, target):
            sum_ = 0
            left = start
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    # Number of two numbers including left
                    sum_ += right - left
                    # Finished this left, so increment the left
                    left += 1
                else:
                    right -= 1

            return sum_

        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            # First subtract one number (nums[i]) from target, and
            # let the functions find other two numbers to meet the criteria
            # with the reduced target and from i + 1
            ans += two_sum_smaller(nums, i + 1, target - nums[i])
        return ans


"""
- Time is O(n^2) for the for loop and nested while loop, and O(nlogn) for sort nums
- Space is O(n)
"""


nums = [-2,0,1,3]
target = 2
print(Solution().threeSumSmaller(nums, target))
