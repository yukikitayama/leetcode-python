"""
[[1,2],[2,3],[3,4],[1,3]]
Sort
[[1,2],[1,3], [2,3],[3,4]]

[-73,      -26]
 [-62, -49]
             [-40, -26]
T: O(NlogN)
S: O(N)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Edge
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: (x[1], x[0]))

        # print(intervals)

        ans = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] < prev_end:
                ans += 1

            else:
                prev_end = intervals[i][1]

        return ans