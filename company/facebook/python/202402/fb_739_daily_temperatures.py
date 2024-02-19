"""
Stack
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = [None] * len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                days = i - prev
                ans[prev] = days

            stack.append(i)

        while stack:
            index = stack.pop()
            ans[index] = 0

        return ans
