"""
sliding window
  k length
  keep the count of B in the window
  record max so far
return k minus max so far
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_so_far = 0
        num_blacks = 0
        left = 0
        for right in range(len(blocks)):

            if blocks[right] == "B":
                num_blacks += 1

            if right - left + 1 > k:
                num_blacks -= int(blocks[left] == "B")
                left += 1

            max_so_far = max(
                max_so_far,
                num_blacks
            )

        return k - max_so_far