"""
[[1,2],[2,3],[3,4],[1,3]]
After sorting in ascending end, and then ascendng start
  [-73, -26], [-62, -49]
  -> [-62, -49], [-73, -26]
[[1,2],[1,3], [2,3],[3,4],]
Stack
  [[1, 2]]
  [[1, 2]. [2, 3]]
  [[1, 2]. [2, 3], [3, 4]]
  num of non-overlapping
Return
  length of intervals - resulted num of non-overlapping = number of intervals removed

T: O(NlogN), length of intervals: N
S: O(2N) -> O(N)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))

        # print("sorted intervals", intervals)

        ans = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] < prev_end:
                ans += 1
            else:
                prev_end = intervals[i][1]

        return ans

    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))

        # print("sorted intervals", intervals)

        stack = []

        for i in range(len(intervals)):

            if stack and intervals[i][0] < stack[-1][1]:
                continue
            else:
                stack.append(intervals[i])

        # print("resulted stack", stack)

        return len(intervals) - len(stack)