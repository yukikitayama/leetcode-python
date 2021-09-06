from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_start, new_end = newInterval
        idx = 0
        n = len(intervals)
        output = []

        # Add all the intervals before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        # Add newInterval without any adjustment
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # Add newInterval with adjustment, overwrite
        else:
            output[-1][1] = max(output[-1][1], new_end)

        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # If no overlap, no adjustment
            if output[-1][1] < start:
                output.append(interval)
            # If overlap
            else:
                output[-1][1] = max(output[-1][1], end)

        return output


"""
Time complexity
Let n the number of intervals, O(n) to one pass the input array

Space complexity
O(n) to keep the output list of intervals
"""


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(Solution().insert(intervals, newInterval))
