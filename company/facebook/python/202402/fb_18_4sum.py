"""
[-2, -1, 0, 0, 1, 2]
"""

from typing import List
import collections


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def two_sum(nums, target):
            """nums is sorted, returns list of two numbers, finds multiple"""
            ans = []

            left = 0
            right = len(nums) - 1

            while left < right:
                sum_ = nums[left] + nums[right]

                if sum_ < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1

                elif sum_ > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1

                else:
                    ans.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

            return ans

        def k_sum(nums, target, k):
            ans = []

            # Edge
            if not nums:
                return ans

            # Edge
            if k == 2:
                return two_sum(nums, target)

            # Edge
            avg = target // k
            # avg < nums[0] means numbers in nums are too large, because smallest number is bigger than average
            # nums[-1] < avg means numbers in nums are too small, because largest number is smaller than average
            if avg < nums[0] or nums[-1] < avg:
                return ans

            for i in range(len(nums)):

                if i == 0 or nums[i] != nums[i - 1]:

                    for subset in k_sum(nums[i + 1:], target - nums[i], k - 1):
                        ans.append([nums[i]] + subset)

            return ans

        nums.sort()

        return k_sum(nums, target, 4)

    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(nums)
        keys = list(counter.keys())
        ans = []

        def backtracking(curr_comb, curr_sum, index):

            if len(curr_comb) == 4 and curr_sum == target:
                ans.append(curr_comb[:])
                return

            if len(curr_comb) > 4:
                return

            for i in range(index, len(keys)):

                k = keys[i]

                if counter[k] > 0:
                    curr_comb.append(k)
                    counter[k] -= 1

                    backtracking(curr_comb, curr_sum + k, i)

                    curr_comb.pop()
                    counter[k] += 1

        backtracking([], 0, 0)

        return ans
