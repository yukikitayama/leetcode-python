"""
Problem
  When h is equal to length of pile, need to eat max of them
  When h is bigger than length of pile, koko can eat slowly
  I can change the order of the piles
  eg1 27 bananas, 27 / 8 = 3 and 3 remaining
  k
    1 <= k <= max value
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # k = 1

        # while True:

        #     hours = 0

        #     for pile in piles:

        #         hours += math.ceil(pile / k)

        #     if hours <= h:
        #         return k

        #     k += 1

        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left