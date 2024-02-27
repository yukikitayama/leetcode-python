"""
Backtracking
set of tuples

Hashmap?
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):

            # Avoid duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curr = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_ = nums[left] + nums[right]

                if curr + sum_ == 0:
                    ans.append([curr, nums[left], nums[right]])
                    left += 1
                    # Avoid duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif curr + sum_ < 0:
                    left += 1

                elif curr + sum_ > 0:
                    right -= 1

        return ans

    def threeSum1(self, nums: List[int]) -> List[List[int]]:

        ans = set()

        nums.sort()

        def backtracking(index, curr):

            if len(curr) == 3 and sum(curr) == 0:
                ans.add(tuple(curr))
                return

            if len(curr) > 3:
                return

            if len(curr) == 3 and sum(curr) != 0:
                return

            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, [])

        return [list(comb) for comb in ans]