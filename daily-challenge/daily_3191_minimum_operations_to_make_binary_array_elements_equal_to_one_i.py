"""
parity invariance
"""

from typing import List
import collections


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for i in range(2, len(nums)):

            if nums[i - 2] == 0:
                ans += 1
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == len(nums):
            return ans
        else:
            return -1

    def minOperations1(self, nums: List[int]) -> int:
        queue = collections.deque()
        ans = 0
        for i in range(len(nums)):

            while queue and i > queue[0] + 2:
                queue.popleft()

            if (nums[i] + len(queue)) % 2 == 0:

                if i + 2 >= len(nums):
                    return -1

                # ?
                ans += 1
                queue.append(i)

        return ans