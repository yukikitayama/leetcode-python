"""
- intervals is already sorted
- iteration
"""

from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        start_remove, end_remove = toBeRemoved

        ans = []

        for start, end in intervals:

            # When current interval is left of remove interval or
            # when current interval is right of remove interval
            if end < start_remove or end_remove < start:
                ans.append([start, end])

            else:
                # when left of remove interval overlaps the current interval
                # Or current interval is in remove interval
                if start < start_remove:
                    ans.append([start, start_remove])

                # when right of remove interval overlaps the current interval
                # Or current interval is in remove interval
                if end_remove < end:
                    ans.append([end_remove, end])

        return ans


if __name__ == '__main__':
    intervals = [[0, 2], [3, 4], [5, 7]]
    toBeRemoved = [1, 6]
    print(Solution().removeInterval(intervals, toBeRemoved))
