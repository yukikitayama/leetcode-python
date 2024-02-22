import collections
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        max_heap = []
        heapq.heapify(max_heap)

        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        ans = []
        while max_heap:
            v, k = heapq.heappop(max_heap)
            ans.append(k * -v)

        return "".join(ans)
