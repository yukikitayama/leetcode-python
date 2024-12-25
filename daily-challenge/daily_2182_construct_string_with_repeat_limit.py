"""
Heap
"""

import collections
import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = []
        for ch, c in collections.Counter(s).items():
            heapq.heappush(max_heap, (-ord(ch), c))

        ans = []
        while max_heap:

            ch_num, c = heapq.heappop(max_heap)
            ch = chr(-ch_num)
            use = min(c, repeatLimit)
            ans.append(ch * use)

            # Insert a different character to be able to keep building and lexicographically large
            if c > use and max_heap:
                next_ch_num, next_c = heapq.heappop(max_heap)
                ans.append(chr(-next_ch_num))

                if (next_c - 1) > 0:
                    heapq.heappush(max_heap, (next_ch_num, next_c - 1))

                heapq.heappush(max_heap, (ch_num, c - use))

        return "".join(ans)
