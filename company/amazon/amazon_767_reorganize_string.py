"""
max heap [(n, char), ...]
pop twice
"""

import heapq
import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        max_heap = []
        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        ans = []

        while max_heap:

            curr_count, curr_char = heapq.heappop(max_heap)
            curr_count *= -1

            if ans and ans[-1] == curr_char:
                if max_heap:
                    next_count, next_char = heapq.heappop(max_heap)
                    next_count *= -1
                    ans.append(next_char)
                    next_count -= 1
                    if next_count > 0:
                        heapq.heappush(max_heap, (-next_count, next_char))
                else:
                    return ""

            ans.append(curr_char)
            curr_count -= 1

            if curr_count > 0:
                heapq.heappush(max_heap, (-curr_count, curr_char))

        # return "".join(ans) if len(ans) == len(s) else ""
        return "".join(ans)
