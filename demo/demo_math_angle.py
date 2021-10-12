"""
math.atan2() returns a number between -pi and pi of the angle
between a point and positive x-axis

"""

import math


# Suppose we face eat, direction pointing at positive x axis from location
location = [1, 1]
# point = [2, 2]
# point = [1, 2]
point = [2, 0]
# point = [-1, 1]

height = point[1] - location[1]
width = point[0] - location[0]
print(f'height: {height}, width: {width}')
print(math.atan2(height, width))
print(math.atan2(height, width) * (180 / math.pi))
theta = math.atan2(height, width) * (180 / math.pi)
print(theta + 360)
print()

location = [1, 1]
# point = [1, 1]
point = [2, 1]
y = point[1] - location[1]
x = point[0] - location[0]
print(f'x: {x}, y: {y}')

ans = math.atan2(y, x)
print(f'ans: {ans}')