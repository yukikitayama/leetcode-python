"""
Points should be even
Sort points by x
Get shift number from leftmost and rightmost average
Iterate from left to half
  Check whether left ith point is reflection of first last
    x == -1 * x
    y == y
    If not meeting, just return false
Return true

e.g.
  (0, 0), (2, 0)
  Shift left by -1
  (-1, 0), (1, 0)
  (0 + 2) / 2 = 1

  (0, 0), (4, 0)
  (0 + 4) / 2 = 2
  shift by -2
  (-2, 0), (2, 0)

  [(0, 0), (1, 0), (3, 0), (4, 0)]
  (0 + 4) / 2 = 2

  [(-2, 0), (-1, 0), (1, 0), (2, 0)]

  [[1,2], [1,4], [2,2],[2,4]]
"""

from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # Remove duplicate
        points = set([tuple(p) for p in points])

        # Find mid
        min_x = float("inf")
        max_x = float("-inf")
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
        mid = (min_x + max_x) / 2

        # For every points, we check if mirrored point exists
        for x, y in points:

            # [1, 3], mid: 2
            # 2 + (2 - 1) = 3
            # 2 + (2 - 3) = 1
            mirror_x = mid + (mid - x)

            if (mirror_x, y) not in points:
                return False

        return True

    def isReflected1(self, points: List[List[int]]) -> bool:

        # Edge
        if len(points) == 1:
            return True

        # Edge
        # if len(points) % 2 != 0:
        #     return False

        # Remove duplicate
        points_set = set()
        for i in range(len(points)):
            points_set.add((points[i][0], points[i][1]))
        points = list(points_set)

        points.sort()

        # Edge
        # if points[0][0] == points[-1][0]:
        #     return True

        first_list = points[:len(points) // 2]
        first_list.sort()

        second_list = points[len(points) // 2:]
        second_list.sort(key=lambda x: (x[0], -x[1]))

        points = first_list + second_list

        # points.sort()

        print(points)

        shift = (points[0][0] + points[-1][0]) / 2

        for i in range(len(points) // 2):

            left_x, left_y = points[i]
            right_x, right_y = points[-(i + 1)]

            left_x -= shift
            right_x -= shift

            if left_x == 0 and right_x == 0:
                continue

            if left_x != -1 * right_x:
                return False

            if left_y != right_y:
                return False

        # Odd
        if len(points) % 2 != 0:
            if points[len(points) // 2][0] - shift == 0:
                return True
            else:
                return False

        # Even
        else:
            return True

