"""
heap to collect intervals
if overlap
  remove longer interval
Overlap
  if curr start < prev end
  if curr end > prev start
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans = 0
        prev = 0
        i = 1

        while i < len(intervals):

            # Overlap if current interval start is earlier than previous interval end
            if intervals[prev][1] > intervals[i][0]:
                ans += 1

                # If previous interval ends after current interval
                # To minimize overlap, remove previous interval and use the current interval
                # which ends earlier, so less chance to overlap
                if intervals[prev][1] > intervals[i][1]:
                    prev = i

            # Not overlap, go to next adjacent pair
            else:
                prev = i

            i += 1

        return ans
