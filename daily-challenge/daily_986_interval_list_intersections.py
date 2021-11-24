"""
- While loop and two pointers
- Time O(n)
- Move one of the two pointers when interval end is smaller
  - When interval is long and it cover multiple intervals in the other lise,
    interval end can cover them,
  - If condition is interval start is smaller, it ignores the above situation.
"""


from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        ans = []
        while p1 < len(firstList) and p2 < len(secondList):
            first = firstList[p1]
            second = secondList[p2]

            start = max(first[0], second[0])
            end = min(first[1], second[1])

            if end >= start:
                ans.append([start, end])

            if first[1] < second[1]:
                p1 += 1
            else:
                p2 += 1

        return ans


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
firstList = [[1,3],[5,9]]
secondList = []
firstList = []
secondList = [[4,8],[10,12]]
firstList = [[1,7]]
secondList = [[3,10]]

firstList = [[3,5],[9,20]]
secondList = [[4,5],[7,10],[11,12],[14,15],[16,20]]
# [[4,5],[9,10],[11,12],[14,15],[16,20]]
"""
        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20
first           ---------               ----------------------------------------------
second              -----       --------------  ------      ------  ------------------
"""
print(Solution().intervalIntersection(firstList, secondList))



