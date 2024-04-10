"""
Sort potions
  Find leftmost index which satisfying product condition
    potion length - the index is the number of pairs for current spell
  Binary search
    if product > success
      search left
    if product < success
      search right
    if product == success
      search left because there could be duplicated potion
"""

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binary_search(spell, target):
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                product = spell * potions[mid]

                if product > success:
                    right = mid - 1
                elif product < success:
                    left = mid + 1
                elif product == success:
                    right = mid - 1

            return left

        ans = []
        for i in range(len(spells)):
            # Binary search
            j = binary_search(spells[i], spells[i] * success)

            num_success = len(potions) - j

            ans.append(num_success)

        return ans