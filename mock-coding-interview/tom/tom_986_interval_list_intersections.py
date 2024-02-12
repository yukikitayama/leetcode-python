"""
intersection
  start: max of start
  end: min of end

not intersection
  end < start

[1, 2]
[1, 2]
"""

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        p1 = 0
        p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):

            interval1 = firstList[p1]
            interval2 = secondList[p2]

            start = max(interval1[0], interval2[0])
            end = min(interval1[1], interval2[1])

            if start <= end:
                overlap = [start, end]
                ans.append(overlap)

            if interval1[1] < interval2[1]:
                p1 += 1
            else:
                p2 += 1

        return ans
