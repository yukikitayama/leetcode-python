"""
stack
if prev is positive, and current is negative, collision
  if current magnitude is smaller, don't append current
  if current magnitude is bigger, keep popping from stack until
    empty
    or current destroyed
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        ans = []

        for a in asteroids:

            while ans and ans[-1] > 0 and a < 0:

                # Both destroy
                if ans[-1] == abs(a):
                    ans.pop()
                    break

                # Current destroy
                elif ans[-1] > abs(a):
                    break

                # Previous destroy
                elif ans[-1] < abs(a):
                    ans.pop()

            else:
                ans.append(a)

        return ans

    def asteroidCollision1(self, asteroids: List[int]) -> List[int]:
        ans = []

        for curr in asteroids:

            # Collision
            if ans and ans[-1] > 0 and curr < 0:

                # Same magnitude, both destroyed
                if abs(ans[-1]) == abs(curr):
                    ans.pop()

                # Current destroyed
                elif abs(ans[-1]) > abs(curr):
                    continue

                elif abs(ans[-1]) < abs(curr):
                    while ans and ans[-1] > 0 and abs(ans[-1]) < abs(curr):
                        ans.pop()

                    # Here could be
                    # empty,
                    # or prev and curr are the same
                    # or prev magnitude is bigger than curr magnitude

                    # Edge
                    if not ans:
                        ans.append(curr)
                    elif ans and ans[-1] < 0:
                        ans.append(curr)
                    elif ans and abs(ans[-1]) == abs(curr):
                        ans.pop()
                    elif ans and abs(ans[-1]) > abs(curr):
                        continue

            # prev: negative, curr: positive, no collision
            # prev and curr sign are the same, no collision
            else:
                ans.append(curr)

            print(ans)

        return ans