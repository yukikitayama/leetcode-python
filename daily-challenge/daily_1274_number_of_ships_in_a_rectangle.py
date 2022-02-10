"""
- At each level, we make hasShips() calls 4^(level) times
- divide and conquer
  - The number of ships in a given rectangle is the sum of the ships returned by the recursive call to
    each sub-rectangle
"""


import math


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """


class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        # No more recursion if no more sub region
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0

        # No more recursion if current region does not contain ship
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # No more recursion if this region contain a ship and current region is a single point
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2

        # Bottom left, top right, top left, bottom right
        return (
            # Bottom left
            self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
            # Top right
            + self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
            # Top left
            + self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
            # Bottom right
            + self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
        )



print(math.log(1000000, 4))