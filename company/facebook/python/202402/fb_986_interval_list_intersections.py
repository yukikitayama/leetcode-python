"""
One interval can affect multiple other intervals

Algo
  two pointers
    While either pointer in the range of intervals
      If one pointer out of bound, no overlap, so terminate
    Compute intersection
      max start, min end
      if start <= end, form interval and append to ans
    Move pointer whose end is smaller
"""


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
                ans.append([start, end])

            if interval1[1] < interval2[1]:
                p1 += 1
            else:
                p2 += 1

        return ans

