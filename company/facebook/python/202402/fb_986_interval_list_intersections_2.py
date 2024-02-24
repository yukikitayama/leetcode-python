"""
Intersection start: max start
Intersection end: min end

Not intersect
  [1, 2]
         [3, 4]
  start: 3,
  end: 2

Two pointers
  Move pointer of the interval whose end is smaller
"""

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        p1 = 0
        p2 = 0
        ans = []

        while p1 < len(firstList) and p2 < len(secondList):
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])

            if start <= end:
                ans.append([start, end])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return ans

