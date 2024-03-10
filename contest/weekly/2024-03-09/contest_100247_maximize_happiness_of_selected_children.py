"""
Sort happiness descending
Initialize happiness_reducer as 0
Initialize ans as 0
while k is bigger than 0
  Get current hapiness
  Reduce happiness by current reducer
  Increment ans by this hapiness
  Increment reducer by 1
"""

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0

        reducer = 0
        i = 0

        while k > 0:
            # Happiness
            h = happiness[i]
            h -= reducer
            h = max(0, h)

            # print(f"h: {h}")

            # Add
            ans += h

            # Next iteration
            i += 1
            k -= 1
            reducer += 1

        return ans