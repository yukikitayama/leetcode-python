"""
- Because we fix the starting point i and draw a line with other points,
  if the slopes are the same, those other points on the same line. We
  do not have to worry about the parallel line with the same slope,
  because parallel lines do not have the same starting point it.
- Slope
  - When two points are vertical, e.g. (x1: 1, y1: 2), (x2: 1, y2: 3),
    slope is (3 - 2) / (1 - 1), division by zero.
  - coprime. a and b are coprime if 1 is the only common divisor. e.g.
    3 and 7 are coprime. 3 and 6 are not, because they also have 3 as
    the common divisor as well as 1, so 1 (3/3) and 2 (6/3) are coprime.
    - So the lines with slop 1/3, 2/6, and 3/9 are all treated as (1, 3)
"""


from typing import List
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # Edge case if the number of points is less than 3.
        # 1 point is just one, and 2 points can definitely be
        # on the same line
        n = len(points)
        if n < 3:
            return n

        def max_points_on_a_line_containing_point_i(i):

            def slope_coprime(x1, y1, x2, y2):
                delta_x = x1 - x2
                delta_y = y1 - y2

                # When delta_x is 0, it's vertical line. The math.gcd() will make
                # different combination, e.g. (0, 1), (0, 2), ..., and they will
                # be treated different slope even if they are the same. So treat
                # this as a special case
                if delta_x == 0:
                    return (0, 0)

                # When delta_y is 0, it's horizontal line. The math.gcd() will make
                # different combination, e.g. (1, 0), (2, 0), ..., even if they are
                # the same slope, so treat this as the second special case
                elif delta_y == 0:
                    return (float('inf'), float('inf'))

                # Because it saves the slope as a tuple of (delta_x, delta_y),
                # the signs are different depending on the relative position
                # of the base point i. The below the slopes are the same -1,
                # but tuples are (-1, 1) and (1, -1). So by keeping delta_x
                # always positive, we can keep the same tuples for the same
                # slopes.
                # e.g. i: (3, 2), i+1: (2, 3), i+2: (4, 1)
                # i+1: delta_x: 1, delta_y: -1
                # i+2: delta_x: -1, delta_y: 1
                elif delta_x < 0:
                    delta_x = -delta_x
                    delta_y = -delta_y

                gcd = math.gcd(delta_x, delta_y)
                slope = (delta_x / gcd, delta_y / gcd)
                return slope

            def add_line(i, j, count):
                x1, y1 = points[i]
                x2, y2 = points[j]

                slope = slope_coprime(x1, y1, x2, y2)

                # Python dictionary.get(key, value), value is the default value
                # if the key does not exist. If the key does not exist, the current
                # (x1, y1) and (x2, y2) newly make a line so the count of points are
                # lines.get(slope, 1) + 1 = 1 + 1 = 2
                # If the key already exists, meaning previously for example there were
                # 2 points, add one new point, so, lines.get(slope, 1) + 1 = 2 + 1 = 3
                lines[slope] = lines.get(slope, 1) + 1

                count = max(lines[slope], count)

                return count

            lines = {}
            count = 1

            for j in range(i + 1, n):
                count = add_line(i, j, count)
            return count

        # Safe to initialize it to 1 because one points can form one answer
        ans = 1

        # n - 1 because the last point do not have another point to connect
        # so the second last point is the last iteration to connect with the
        # last point
        for i in range(n - 1):
            ans = max(ans, max_points_on_a_line_containing_point_i(i))

        return ans


points = [[1,1],[2,2],[3,3]]  # 3
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  # 4
points = [[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]]  # 7
"""
4*
3
2
1*
0*
-1*
-2*
-3*
-4*
"""
print(Solution().maxPoints(points))

