from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Edge case
        if not intervals:
            return [newInterval]

        # Insert new interval to keep ascending order
        stack = []
        inserted = False
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                stack.append(newInterval)
                inserted = True
            stack.append(intervals[i])

        if not inserted:
            stack.append(newInterval)

        # Fix overlapping intervals
        ans = []
        for i in range(len(stack)):
            if ans and ans[-1][1] >= stack[i][0]:
                ans[-1][1] = max(ans[-1][1], stack[i][1])
            else:
                ans.append(stack[i])

        return ans
