"""
Brute force
Formula
1/2 * abs(xa (yb - yc) + xb(yc - ya) + xc(ya - yb))
"""

from typing import List
import itertools


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0

        for a, b, c in itertools.combinations(points, 3):
            ans = max(
                ans,
                1 / 2 * abs(
                    a[0] * (b[1] - c[1])
                    + b[0] * (c[1] - a[1])
                    + c[0] * (a[1] - b[1])
                )
            )

        return ans
