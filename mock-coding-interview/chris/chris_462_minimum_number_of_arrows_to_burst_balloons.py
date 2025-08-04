"""
1------6
 2-------8
        7-----12
            10------16

1------6
 2---5
        7-----12
            10------16

1------6
 2---5
       6-----12
            10------16


1---2
      3---4
            5---6
                  7---8

points = [[1, 1]]

Stack
  max start, min end
  if curr start <= prev end
    update stack top
      max start, min end
  if curr start > prev end
    append a new interval to stack
return length of stack
T: O(NlogN), S: O(N)
eg1
  [[1, 6]]
  []
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        # stack = [points[0]]
        prev_start = points[0][0]
        prev_end = points[0][1]
        ans = 1

        for i in range(1, len(points)):

            # if points[i][0] <= stack[-1][1]:
            if points[i][0] <= prev_end:
                # stack[-1][0] = max(stack[-1][0], points[i][0])
                prev_start = max(prev_start, points[i][0])
                # stack[-1][1] = min(stack[-1][1], points[i][1])
                prev_end = min(prev_end, points[i][1])

            else:
                # stack.append([points[i][0], points[i][1]])
                ans += 1
                prev_start = points[i][0]
                prev_end = points[i][1]

        # return len(stack)
        return ans