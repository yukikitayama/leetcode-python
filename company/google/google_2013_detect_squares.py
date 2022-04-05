"""
- Axis-aligned square is a square
"""


from typing import List
import collections


class DetectSquares:

    def __init__(self):
        self.count_points = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.count_points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point

        for (x3, y3), count in self.count_points.items():
            # If point is overlapped, no shape
            # If width and height are different, not square
            if abs(x1 - x3) == 0 or abs(x1 - x3) != abs(y1 - y3):
                continue

            # Find how many we have for point2 and point4 position
            ans += count * self.count_points[(x1, y3)] * self.count_points[(x3, y1)]

        return ans
