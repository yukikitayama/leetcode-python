"""
If we skip closing the first open door
  and take here as starting point
  every time we see the next open door house
    we compute the distance from the starting point to here
    it could be distance between 2 hourses,
    or it could be circle back and the distance is from first open house to the same open house
  if first open house is the rightmost of the array
    from then it might gonna take k steps to come back, but it already spent almost k steps
    So we need 2k steps to come back regardless of the location of the first open house
"""

from typing import Optional

# Definition for a street.
class Street:
    def closeDoor(self):
        pass
    def isDoorOpen(self):
        pass
    def moveRight(self):
        pass


class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        i = 0
        found_first_open = False

        while i <= k * 2:

            if street.isDoorOpen():

                if found_first_open:
                    dist_from_first = i - first_open_idx
                    street.closeDoor()

                elif not found_first_open:
                    found_first_open = True
                    first_open_idx = i

            street.moveRight()
            i += 1

        return dist_from_first
