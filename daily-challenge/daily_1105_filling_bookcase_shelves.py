"""
dp(i, current height, current width)
  if i is length of books
    return 0

  Recurrence transition
    include next book at the current level
      if current width + next book width <= shlfWidth
        dp(i + 1, max(current height, next book height), current width + next width)
    include next book at the next level
      current_height + dp(i + 1, next height, next width)
"""

from typing import List
import functools


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        @functools.lru_cache
        def dp(index, curr_height, curr_width):

            # print(f"index: {index}, curr_height: {curr_height}, curr_width: {curr_width}")

            if index == len(books):
                return curr_height

            res = float("inf")

            # Add current book to current level
            if curr_width + books[index][0] <= shelfWidth:
                res = min(
                    res,
                    dp(index + 1, max(curr_height, books[index][1]), curr_width + books[index][0])
                )

            # Add current book to another level
            res = min(
                res,
                curr_height + dp(index + 1, books[index][1], books[index][0])
            )

            return res

        return dp(0, 0, 0)