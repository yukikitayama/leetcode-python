"""
prev = 0
for loop iterate arr
  if curr - prev > 1:
      diff = curr - prev
      while k > 0 and diff - 1 > 0
        prev += 1
        k -= 1
        if k == 0
          return prev
        diff -= 1
  prev = curr
If k still > 0,
  nums[-1] + k
"""

from typing import List


class Solution:
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     prev = 0

    #     for i in range(len(arr)):
    #         curr = arr[i]
    #         diff = curr - prev

    #         # Wnere there are missing
    #         if diff > 1:
    #             while k > 0 and diff - 1 > 0:
    #                 prev += 1
    #                 k -= 1
    #                 diff -= 1

    #                 if k == 0:
    #                     return prev

    #         prev = curr

    #     if k > 0:
    #         return arr[-1] + k

    def findKthPositive(self, arr: List[int], k: int) -> int:

        # If kth missing exist before arr
        if k < arr[0]:
            return k

        # If in arr
        k -= arr[0] - 1
        for i in range(len(arr) - 1):
            count_missing = arr[i + 1] - arr[i] - 1

            if k <= count_missing:
                return arr[i] + k

            k -= count_missing

        # If kth missing exist after arr
        if k > 0:
            return arr[-1] + k