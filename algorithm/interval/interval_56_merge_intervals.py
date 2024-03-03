from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        ans.append(intervals[0])

        for i in range(1, len(intervals)):

            # Overlap
            if ans[-1][1] >= intervals[i][0]:
                # Merge
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

            else:
                ans.append(intervals[i])

        return ans