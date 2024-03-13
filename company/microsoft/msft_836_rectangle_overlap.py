"""
horizontal
  a.x2 > b.x1 and a.y2 > b.y1
  b.x2 > a.x1 and
  max(a.x1, b.x1) < min(a.x2, b.x2)
vertical
  a.y2 > b.y1
  b.y2 > a.y1
"""

from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if (
                max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
                and max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        ):
            return True
        else:
            return False
