import collections
import heapq


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)

        ans = []
        for i in range(len(order)):
            ch = order[i]
            if ch in counter:
                ans.append(ch * counter[ch])
                del counter[ch]

        for k, v in counter.items():
            ans.append(k * v)

        return "".join(ans)

    def customSortString1(self, order: str, s: str) -> str:
        ch_to_order = {order[i]: i for i in range(len(order))}
        counter = collections.Counter(s)
        min_heap = []
        for k, v in counter.items():
            if k in ch_to_order:
                heapq.heappush(min_heap, (ch_to_order[k], k, v))
            else:
                heapq.heappush(min_heap, (26, k, v))

        ans = []
        while min_heap:
            o, ch, count = heapq.heappop(min_heap)
            ans.append(ch * count)

        return "".join(ans)