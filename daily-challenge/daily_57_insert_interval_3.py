from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        ans.append(newInterval)

        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Edge
        if not intervals:
            return [newInterval]

        ans = []
        inserted = False

        # Edge
        if newInterval[0] < intervals[0][0]:
            ans.append(newInterval)
            inserted = True

        for i in range(len(intervals)):

            interval = intervals[i]

            if not inserted and interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= \
                    interval[1]:
                interval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                inserted = True
                ans.append(interval)

            elif ans and ans[-1][0] <= interval[0] <= ans[-1][1] or ans[-1][0] <= interval[1] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])

            else:
                ans.append(interval)

        # Edge
        if not inserted:
            ans.append(newInterval)
            return ans

        else:
            return ans
