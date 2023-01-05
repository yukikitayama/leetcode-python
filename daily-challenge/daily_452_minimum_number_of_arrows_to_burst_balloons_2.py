"""
- sort points and count how many overlaps
"""


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        curr_end = points[0][1]

        # Initialize to be 1 because it's incremented when the next arrow is needed
        ans = 1

        for start, end in points:

            if curr_end < start:
                ans += 1
                curr_end = end

        return ans





