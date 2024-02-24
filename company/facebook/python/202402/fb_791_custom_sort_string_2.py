"""
Hashmap
  k: order char
  v: index in order string as order

Min heap
  (s char, order index)
  if s char not in hashmap, 26 order
"""

import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # ch_to_order = collections.defaultdict(int)
        # for i in range(len(order)):
        #     ch_to_order[order[i]] = i

        # min_heap = []
        # heapq.heapify(min_heap)
        # for i in range(len(s)):

        #     if s[i] in ch_to_order:
        #         heapq.heappush(min_heap, (ch_to_order[s[i]], s[i]))
        #     else:
        #         heapq.heappush(min_heap, (26, s[i]))

        # ans = []
        # for i in range(len(min_heap)):
        #     o, c = heapq.heappop(min_heap)
        #     ans.append(c)

        # return "".join(ans)

        counter = collections.Counter(s)

        ans = []

        for ch in order:
            if ch in counter:
                ans.append(ch * counter[ch])

        order_set = set(order)
        for ch in counter:
            if ch not in order_set:
                ans.append(ch * counter[ch])

        return "".join(ans)