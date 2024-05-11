"""
Hashmap
  k: character
  v: remaing count of the character

Greedy
  Use character which has higher counts
  but if prev character is the same as current character, I'm choosing the next highest counts character

s: "abacad"
  a: 0
  b: 0
  c: 0
  d: 0
    a, b, a, c, a, d
"""

import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = collections.Counter(s)
        max_heap = []
        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        ans = []
        prev = None
        while max_heap:

            curr_count, curr_char = heapq.heappop(max_heap)
            curr_count *= -1

            if curr_char != prev:
                ans.append(curr_char)
                curr_count -= 1

                if curr_count > 0:
                    heapq.heappush(max_heap, (-curr_count, curr_char))

                prev = curr_char

            else:
                if len(max_heap) == 0:
                    return ""

                next_count, next_char = heapq.heappop(max_heap)
                next_count *= -1

                ans.append(next_char)
                next_count -= 1
                if next_count > 0:
                    heapq.heappush(max_heap, (-next_count, next_char))

                heapq.heappush(max_heap, (-curr_count, curr_char))

                prev = next_char

        return "".join(ans)