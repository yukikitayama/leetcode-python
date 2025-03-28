"""
append the first k - 1 elements to colors
sliding window
  expand current is different from previous
  if current is same as the previous
    contact left pointer to current position
  if length is bigger than k
    contract by one
  if length is k, increment answer
"""

from typing import List


class Solution:

    def numberOfAlternatingGroups1(self, colors: List[int], k: int) -> int:
        extended_colors = colors + colors[:k - 1]

        # print(extended_colors)

        ans = 0
        left = 0
        for right in range(len(extended_colors)):

            if right > 0 and extended_colors[right] == extended_colors[right - 1]:
                left = right

            if right - left + 1 > k:
                left += 1

            if right - left + 1 == k:
                ans += 1

        return ans