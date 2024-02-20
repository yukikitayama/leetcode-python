"""
stack
  for loop iteration
  append if positive
  if negative
    if top is bigger than abs curr negative
      skip curr negative
    if top is smaller
      pop top
      keep comparin
return stack as answer

Ans
  Collision occurs only when stack top is positive and current is negative
  When stack top is negative and current is positive, they won't collide
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in range(len(asteroids)):

            curr = asteroids[i]

            # Top is going right, curr is going left, so collide
            while stack and stack[-1] > 0 and curr < 0:

                # Both explode
                if stack[-1] == abs(curr):
                    stack.pop()
                    # When break happens in while else loop, else won't execute
                    break

                # Left explodes, but right stays
                elif stack[-1] < abs(curr):
                    stack.pop()
                    continue

                # Left stays, but right explode
                elif stack[-1] > abs(curr):
                    # When break happens in while else loop, else won't execute
                    break

            else:
                stack.append(curr)

        return stack
