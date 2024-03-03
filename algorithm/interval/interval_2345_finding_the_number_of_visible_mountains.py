"""
1: [6, 3]
2: [5, 4]

x + y diagonal
x - y anti diagonal

eg: [3, 2]
  5 - 4 = 1
  3 - 2 = 1

If current x + y or x - y overlaps with the existing x + y or x - y,
  if current y < existing y
    current cannot be visible
  if current y > existing y
    existing is not visible
  if current y == existing y
    both are not visible

Heap?
  [(plus, height, index), (minus, height, index)]
"""

from typing import List
import collections


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:

        counter = collections.Counter()

        for x, y in peaks:
            counter[(x, y)] += 1

        # Sort unique (x, y) by ascending
        peaks = sorted(counter.keys())

        if not peaks:
            return 0

        # print(peaks)

        def is_right_within_left(point_a, point_b):
            x_a, y_a = point_a
            x_b, y_b = point_b

            # diagonal and anti diagonal values are the y values at x = 0
            diagonal = x_a + y_a
            anti_diagonal = y_a - x_a

            # diagonal - x because slope is negative
            # anti diagonal + x because slope is positive
            return y_b <= diagonal - x_b and y_b <= anti_diagonal + x_b

        stack = []
        stack.append(peaks[0])

        for x, y in peaks[1:]:

            # If previous point is within current point
            # Remove previous point
            while stack and is_right_within_left((x, y), stack[-1]):
                stack.pop()

            # If current point is not within previous
            # Add
            if not stack or not is_right_within_left(stack[-1], (x, y)):
                stack.append((x, y))

        # Only count non-overlapping points
        ans = 0
        for i in range(len(stack)):
            p = stack[i]

            if counter[p] == 1:
                ans += 1

        return ans
