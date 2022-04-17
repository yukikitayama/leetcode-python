"""
- Two pointers sliding window
"""


from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        left = 0
        right = 0
        sum_left = 0
        sum_right = 0
        ans = 0

        for j, num in enumerate(nums):

            sum_left += num

            while left < j and sum_left > goal:
                sum_left -= nums[left]
                left += 1

            sum_right += num
            while right < j and (sum_right > goal or sum_right == goal and not nums[right]):
                sum_right -= nums[right]
                right += 1

            if sum_left == goal:
                ans += right - left + 1

        return ans


if __name__ == '__main__':
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(Solution().numSubarraysWithSum(nums, goal))
