"""
- As if my location is origin at xy plane, subtract my location x and y from x and y of each point
- Use atan2 functions to get degree around origin from positive x axis to the point
  - the given angle is degree from 0 to 360
  - Save all the degrees to an array
  - It gives us the number from 0 to 360
  - We wanna capture points for example at 350 degrees with 10 degrees, append another cycle to the array
- Initialize ans to 0
- If a point is on my location, increment ans
- From the array, with the given angle, find the maximum number points to capture
    - Use two pointers, initially left and right to 0
    - Set base to degrees[left] + angle
    - Initialize max_so_far to 0
    - Iterate degree in degrees from 1 to len(degrees) exclusive
      - if degrees[right] <= base,
        - ans = max(ans, max_so_far),
        - increment right
      - if degrees[right] > base,
        - increment left
        - Update base to degrees[left] + angle
        - Reset max_so_far to 1

Test
- For example, angle: 90, degrees: [15, 45, 165, 355, 375(15), 405(45)],
  the maximum number is 3 by 355, 375 (15) and 405 (45)
ans: 0, left: 0, right: 0, max_so_far = 1
base: degrees[left] + angle: 105
right: 1, degrees[right]: 45, 45 <= 105: T, max_so_far: 2, ans: max(ans, max_so_far) = 2, right: 3
right: 3, degrees[right]: 165, 165 <= 105: F, left: 1, base: degrees[left] + angle: 45 + 90 = 135, max_so_far: 1
"""


from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        def get_degree(x_location, y_location, x_point, y_point):
            x = x_point - x_location
            y = y_point - y_location
            # math.atan2 gives us the 0 to 3.14 from positive x axis, go up and to negative x axis
            # math.atan2 gives us the 0 to -3.14 from positive x axis, go down, and to negative x axis
            degree = math.atan2(y, x) * (180 / math.pi)
            # If it's negative, add 360 as if we visit the negative point by traversing from
            # positive x axis, go up and negative x axis, and go down
            if degree < 0:
                degree += 360
            return degree

        # Exclude the points which locate at my location
        initial_length = len(points)
        points = [point for point in points if point != location]
        points_on_me = initial_length - len(points)

        # print(f'points: {points}')

        degrees = []
        for point in points:
            degree = get_degree(location[0], location[1], point[0], point[1])
            degrees.append(degree)

        # print(f'degrees: {degrees}')

        # Sort the array for the later for loop
        degrees.sort()

        # Append another cycle
        extended_degrees = [degree for degree in degrees]
        for degree in degrees:
            next_degree = degree + 360
            extended_degrees.append(next_degree)

        # print(f'sorted and another cycle appended degrees: {extended_degrees}')

        # Find maximum number of points in view
        ans = 0
        left = right = 0

        while right < len(extended_degrees):

            while right < len(extended_degrees) and extended_degrees[right] - extended_degrees[left] <= angle:
                right += 1

            ans = max(ans, right - left)

            while right < len(extended_degrees) and left < right and extended_degrees[right] - extended_degrees[left] > angle:
                left += 1

        return ans + points_on_me


points = [[2,1],[2,2],[3,3]]
angle = 90
location = [1,1]
print(Solution().visiblePoints(points, angle, location))



