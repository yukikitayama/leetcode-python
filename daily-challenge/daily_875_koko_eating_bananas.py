from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:

            speed = left + (right - left) // 2
            hour = 0

            for pile in piles:
                hour += math.ceil(pile / speed)

            if hour <= h:
                right = speed
            else:
                left = speed + 1

        return right


"""
- Let m be the max pile and n be the length of piles
- Time is O(nlogm) because search space gets half between 1 and m, so O(logm)
  and each time iterate piles, so O(n)
"""
