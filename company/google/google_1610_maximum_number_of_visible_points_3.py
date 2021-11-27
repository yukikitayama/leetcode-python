from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def point_to_degree(x_location: int, y_location: int, x_point: int, y_point: int) -> float:
            y = y_point - y_location
            x = x_point - x_location
            degree = math.atan2(y, x) * (180 / math.pi)

            if degree < 0:
                degree += 360

            return degree

        # Exclude the points on me, because we don't have to do anything special
        num_points = len(points)
        points_except_location = [point for point in points if point != location]
        num_points_at_location = num_points - len(points_except_location)

        if len(points_except_location) == 0:
            return num_points_at_location

        degrees = [point_to_degree(location[0], location[1], point[0], point[1]) for point in points_except_location]

        # Extend it for cycular
        extended_degrees = [degree for degree in degrees]
        for degree in degrees:
            extended_degrees.append(degree + 360)

        # Sort degrees to count number of points in angle
        extended_degrees.sort()

        ans = 0
        left = right = 0

        while right < len(extended_degrees):

            while right < len(extended_degrees) and extended_degrees[right] - extended_degrees[left] <= angle:
                right += 1

            num_view = right - left
            ans = max(ans, num_view)

            while right < len(extended_degrees) and left < right and extended_degrees[right] - extended_degrees[
                left] > angle:
                left += 1

        return ans + num_points_at_location