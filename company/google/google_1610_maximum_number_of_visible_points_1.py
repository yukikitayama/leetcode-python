from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        initial_length = len(points)
        points = [point for point in points if point != location]
        points_on_me = initial_length - len(points)

        def angle_from_me(point):
            x1, y1 = location
            x2, y2 = point
            # as if the heigh and width from the positive x axis
            height = y2 - y1
            width = x2 - x1
            # The below gives us 0 degree from right side and 180 degree to left side
            # Negative if it's below the location
            theta = math.atan2(height, width) * (180 / math.pi)
            # + 360 because we don't wanna negative degree so go round counterclockwise
            return theta if theta >= 0 else theta + 360

        angles = sorted([angle_from_me(point) for point in points])

        # print(f'angles: {angles}')

        if not angles:
            return points_on_me

        # This allows us to see that 355 is close to 0
        # Append the same array because this array is circular.
        # So when it goes to 355 and if there's point at 0, it needs to see
        # 355 and 0 (-> 360) at the same time
        angles += [a + 360 for a in angles]

        # Use sliding window to count the points
        most_points_observable = 0
        i = j = 0

        while j < len(angles):

            while j < len(angles) and angles[j] - angles[i] <= angle:
                j += 1

            most_points_observable = max(j - i, most_points_observable)

            while j < len(angles) and i < j and angles[j] - angles[i] > angle:
                i += 1

        return points_on_me + most_points_observable


"""
Time complexity
Let n be the number of points
O(nlogn) for sorting

Space complexity
O(n) for arrays
"""


points = [[2,1],[2,2],[3,3]]
# points = [[1, 1]]
angle = 90
location = [1,1]
points = [[2,1],[2,2],[3,4],[1,1]]
angle = 90
angle = 45  # 3
location = [1,1]
print(Solution().visiblePoints(points, angle, location))

