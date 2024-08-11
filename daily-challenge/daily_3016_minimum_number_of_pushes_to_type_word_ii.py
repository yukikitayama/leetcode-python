"""
greedy
simulation
26
  lowercase English letters
first 8 characters with the largest number of times
  1
second 8 characters with
  2
third 8
  3
last 2 characters
  4
"""

import collections
import heapq


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = collections.Counter(word)
        max_heap = []
        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        ans = 0
        weight = 1
        count = 0
        while max_heap:

            curr_count, curr_char = heapq.heappop(max_heap)
            curr_count *= -1
            count += 1

            if count == 9:
                weight = 2
            elif count == 17:
                weight = 3
            elif count == 25:
                weight = 4

            ans += curr_count * weight

        return ans
