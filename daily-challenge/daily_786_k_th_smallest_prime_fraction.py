"""
Obs
  sorted
  unique
  [1, 3]
    if numerator moves right, fraction gets bigger
    if denominator moves right, fraction gets smaller
  smallest fraction is leftmost / rightmost
  largest fraction is mid left / mid right
  [1, 2, 3, 5]
    [1, 5], 1/5
    [1, 3] or [2, 5]

Two pointers
  moves toward center
  every step, compare next 2 candidates
  stop after k times

Ans
  Replace current smallest fraction with the next smallest fraction with the same numerator and the decremented denominator
"""

from typing import List
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []

        # Initialize min heap
        for i in range(len(arr) - 1):
            heapq.heappush(min_heap, (arr[i] / arr[len(arr) - 1], i, len(arr) - 1))

        ans = [None] * 2

        while k > 0:
            curr_fraction, nume_idx, deno_idx = heapq.heappop(min_heap)
            k -= 1
            ans[0] = arr[nume_idx]
            ans[1] = arr[deno_idx]

            if nume_idx < deno_idx - 1:
                heapq.heappush(min_heap, (arr[nume_idx] / arr[deno_idx - 1], nume_idx, deno_idx - 1))

        return ans

    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:

        left = 0
        right = len(arr) - 1

        while k > 0:

            ans = [arr[left], arr[right]]
            k -= 1

            if arr[left + 1] / arr[right] < arr[left] / arr[right - 1]:
                left += 1
            else:
                right -= 1

            print(k, ans, left, right)

        return ans
