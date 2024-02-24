from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        ans = [intervals[0]]

        for i in range(1, len(intervals)):

            if intervals[i][0] <= ans[-1][1]:
                end = max(intervals[i][1], ans[-1][1])
                ans[-1][1] = end

            else:
                ans.append(intervals[i])

        return ans
