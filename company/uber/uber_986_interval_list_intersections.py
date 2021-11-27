from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Start, max start to find intersection
            lo = max(firstList[i][0], secondList[j][0])
            # End, min end to find intersection
            hi = min(firstList[i][1], secondList[j][1])

            # If both intervals are not intersected, lo is bigger than hi
            if lo <= hi:
                ans.append([lo, hi])

            # Move the pointer of interval whose ending is earlier
            # to find the next interval intersection
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans


"""
first:  1---2---3---4
second:     2---3
lo: 2, hi, 3

first:  1---2
second:         3---4
lo: 3, hi: 2
"""


# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(Solution().intervalIntersection(firstList, secondList))

