"""
Greedy
max heap
"""

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, "a"))
        if b > 0:
            heapq.heappush(max_heap, (-b, "b"))
        if c > 0:
            heapq.heappush(max_heap, (-c, "c"))

        ans = []

        while max_heap:

            count, ch = heapq.heappop(max_heap)
            count *= -1

            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                if not max_heap:
                    break

                next_count, next_ch = heapq.heappop(max_heap)
                next_count *= -1

                ans.append(next_ch)
                next_count -= 1

                if next_count > 0:
                    heapq.heappush(max_heap, (-next_count, next_ch))

                heapq.heappush(max_heap, (-count, ch))

            else:

                count -= 1
                ans.append(ch)

                if count > 0:
                    heapq.heappush(max_heap, (-count, ch))

        return "".join(ans)