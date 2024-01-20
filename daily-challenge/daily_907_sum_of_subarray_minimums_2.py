"""
How to describe overlapping subproblem
if a range include a particular index
"""

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10 ** 9 + 7
        stack = []
        ans = 0

        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):

                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i

                count = (mid - left) * (right - mid)
                ans += (count * arr[mid])

            stack.append(i)

        return ans % MOD




