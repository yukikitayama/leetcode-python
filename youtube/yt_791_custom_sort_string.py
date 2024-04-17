import collections
import heapq


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)

        ans = []
        for i in range(len(order)):
            if order[i] in counter:
                ans.append(order[i] * counter[order[i]])
                del counter[order[i]]

        for k, v in counter.items():
            ans.append(k * v)

        return "".join(ans)

    def customSortString1(self, order: str, s: str) -> str:
        ch_to_order = {order[i]: i for i in range(len(order))}

        # print(ch_to_order)

        min_heap = []
        heapq.heapify(min_heap)

        for i in range(len(s)):
            if s[i] in ch_to_order:
                heapq.heappush(min_heap, (ch_to_order[s[i]], s[i]))
            else:
                heapq.heappush(min_heap, (26, s[i]))

        # print(min_heap)

        ans = []
        while min_heap:
            o, ch = heapq.heappop(min_heap)
            ans.append(ch)

        return "".join(ans)