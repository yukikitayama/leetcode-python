"""
obs
  meetings can overlap
  meetings are not sorted

sort by start
if first start is smaller than days,
  add start - 1 to day
iterate from left to right, from 2nd element
  if curr start is bigger than prev end
    add day
if last end is smaller than days
  add days - last end
    e.g. [7, 8], days: 10, 10 - 8 = 2

[[1, 3], [5, 7]]
  (5 - 1) - (3 + 1) + 1 = 4 - 4 + 1 = 1
[[1, 3], [2, 4]]
  (2 - 1) - (3 + 1) + 1 = 1 - 4 + 1 = -4
"""

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0
        max_end = 0
        meetings.sort()
        for s, e in meetings:
            if s > max_end + 1:
                ans += s - max_end - 1
            max_end = max(max_end, e)
        ans += days - max_end

        return ans

    def countDays1(self, days: int, meetings: List[List[int]]) -> int:
        ans = 0

        meetings.sort()

        print(meetings)

        max_end = 0

        # First
        if meetings[0][0] < days:
            ans += meetings[0][0] - 1
        max_end = max(meetings[0][1], max_end)

        # Iterate
        for i in range(1, len(meetings)):
            if max_end < meetings[i][0]:
                ans += (meetings[i][0] - 1) - (max_end + 1) + 1
            max_end = max(meetings[i][1], max_end)

        # Last
        if max_end < days:
            ans += (days - max_end)

        return ans