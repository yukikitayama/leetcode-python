import collections
import heapq


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = collections.Counter(s)

        ans = []

        for i in range(order):

            if order[i] in counter:
                ans.append(order[i] * counter[order[i]])
                counter[order[i]] = 0

        for k, v in counter.items():
            if v != 0:
                ans.append(k * v)

        return "".join(ans)

    def customSortString(self, order: str, s: str) -> str:
        ch_to_order = collections.defaultdict(int)

        for i in range(len(order)):
            ch_to_order[order[i]] = i

        min_heap = []
        heapq.heapify(min_heap)

        counter = collections.Counter(s)

        for k, v in counter.items():
            if k in ch_to_order:
                heapq.heappush(min_heap, (ch_to_order[k], k, v))
            else:
                heapq.heappush(min_heap, (26, k, v))

        ans = []

        while min_heap:
            o, c, v = heapq.heappop(min_heap)
            ans.append(c * v)

        return "".join(ans)

    def customSortString1(self, order: str, s: str) -> str:
        ch_to_order = collections.defaultdict(int)

        for i in range(len(order)):
            ch_to_order[order[i]] = i

        min_heap = []
        heapq.heapify(min_heap)

        for i in range(len(s)):

            if s[i] in ch_to_order:
                heapq.heappush(min_heap, (ch_to_order[s[i]], s[i]))
            else:
                heapq.heappush(min_heap, (26, s[i]))

        ans = []

        while min_heap:
            o, c = heapq.heappop(min_heap)
            ans.append(c)

        return "".join(ans)