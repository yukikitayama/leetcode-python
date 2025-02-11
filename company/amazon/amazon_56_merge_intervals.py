"""
sort
if prev end >= curr start
  merge
    modify the last element in stack
      prev end = curr end
otherwise
  append current interval to stack
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for interval in intervals:

            if stack and stack[-1][1] >= interval[0]:
                stack[-1][1] = max(interval[1], stack[-1][1])

            else:
                stack.append(interval)

        return stack
