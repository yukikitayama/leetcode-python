"""
Hashmap
  k: ch
  v: count
Min heap
  get a earlier than b
  [(0, "a"), (0, "b")]
    [(1, "a"), (0, "b")]
    [(0, "b"), (1, "a")]
How to create initial heap
  [(0, "b"), (0, "c"), ..., (2, "a")]
When ?
  Get character from min heap
    increment count
T: O(NlogK)
S: O(N)
"""

import heapq


class Solution:
    def minimizeStringValue(self, s: str) -> str:

        counter = dict()
        for i in range(26):
            counter[chr(ord("a") + i)] = 0

        # print(counter)

        for ch in s:
            if ch != "?":
                counter[ch] += 1

        # print(counter)

        min_heap = []
        for k, v in counter.items():
            heapq.heappush(min_heap, (v, k))

        buffer = []
        for ch in s:

            if ch != "?":
                continue

            else:
                curr_count, curr_char = heapq.heappop(min_heap)
                buffer.append(curr_char)
                curr_count += 1
                heapq.heappush(min_heap, (curr_count, curr_char))

        buffer.sort(reverse=True)
        ans = []
        for ch in s:
            if ch != "?":
                ans.append(ch)
            else:
                b = buffer.pop()
                ans.append(b)

        return "".join(ans)