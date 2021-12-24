from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]

        for i in range(1, len(intervals)):

            curr_start, curr_end = intervals[i]

            if curr_start <= ans[-1][1]:

                start = min(ans[-1][0], curr_start)
                end = max(ans[-1][1], curr_end)
                ans[-1][0] = start
                ans[-1][1] = end

            else:
                ans.append(intervals[i])

        return ans


intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(Solution().merge(intervals))
