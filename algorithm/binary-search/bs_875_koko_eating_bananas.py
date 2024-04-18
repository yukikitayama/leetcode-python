"""
piles = [3,6,7,11], h = 8
k: 11, 4 hours
k: 5, 8 hours (1, 2, 2, 3)
k: 4, 8 hours (1, 2, 2, 3)
k: 3, 10 hours (1, 2, 3, 4)

left: 1
right: max(piles)
binary search
  for each mid num
    count hours
    if hours < h:
      search to left
    if hours > h:
      search to right
    if equal
      search to left, because eat slowly
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:

            k = (left + right) // 2

            hours_need = 0
            for i in range(len(piles)):
                q, r = divmod(piles[i], k)
                hours_need += q
                if r > 0:
                    hours_need += 1

            if hours_need < h:
                right = k - 1
            elif hours_need > h:
                left = k + 1
            elif hours_need == h:
                right = k - 1

        # print(f"left: {left}, right: {right}")

        return left
