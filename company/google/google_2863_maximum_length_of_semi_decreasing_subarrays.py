"""
max so far and its index
if curr is smaller than prev
  extend

dp(i)
  return longest length up to i

Brute force
  Try every two pointers
    if num at right is smaller,
      length = right - left + 1
"""

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        # From top to bottom, strictly increasing
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for i in stack:
            print(nums[i], i)

        ans = 0

        max_so_far = float("-inf")

        print()

        for left in range(len(nums)):

            print(f"left: {left}")

            # Remove invalid right pointer
            while stack and left >= stack[-1]:
                print("invalid")
                stack.pop()

            if nums[left] > max_so_far:
                max_so_far = nums[left]

            # Move right pointer to expand window
            while stack and max_so_far > nums[stack[-1]]:
                print(max_so_far, nums[stack[-1]])
                right = stack.pop()
                ans = max(ans, right - left + 1)

        return ans

    def maxSubarrayLength1(self, nums: List[int]) -> int:
        ans = 0

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] > nums[right]:
                    ans = max(ans, right - left + 1)

        return ans
