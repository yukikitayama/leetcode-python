from typing import List
import functools


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leftmost_good_index = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= leftmost_good_index:
                leftmost_good_index = i
        return leftmost_good_index == 0

    def canJump4(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        # 1 means good
        memo[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            furthest = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest + 1):
                if memo[j] == 1:
                    memo[i] = 1
                    break
        return memo[0] == 1

    def canJump3(self, nums: List[int]) -> bool:

        memo = [-1] * len(nums)

        # Base: It can reach itself
        memo[-1] = True

        def dp(index):

            if memo[index] != -1:
                return memo[index] == 1

            furthest_index = min(index + nums[index], len(nums) - 1)
            for i in range(index + 1, furthest_index + 1):
                if dp(i):
                    memo[index] = 1
                    return True

            memo[index] = 0

            return False

        return dp(0)

    def canJump2(self, nums: List[int]) -> bool:

        @functools.cache
        def dp(index):
            if index == len(nums) - 1:
                return True

            res = False
            furthest_index = min(index + nums[index], len(nums) - 1)
            for i in range(index + 1, furthest_index + 1):
                res |= dp(i)

            return res

        return dp(0)

    def canJump1(self, nums: List[int]) -> bool:

        @functools.cache
        def dp(index):

            if index >= len(nums) - 1:
                return True

            if nums[index] == 0:
                return False

            res = False

            for step in range(1, nums[index] + 1):
                res |= dp(index + step)

            return res

        return dp(0)
