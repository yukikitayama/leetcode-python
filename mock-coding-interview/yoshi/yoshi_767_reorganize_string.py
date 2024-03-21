import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        max_heap = []
        heapq.heapify(max_heap)
        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        ans = []

        while max_heap:

            v_1, k_1 = heapq.heappop(max_heap)

            if ans and ans[-1] != k_1:
                ans.append(k_1)
                v_1 += 1
                if v_1 < 0:
                    heapq.heappush(max_heap, (v_1, k_1))

            else:

                if len(max_heap) == 0:
                    return ""

                else:
                    v_2, k_2 = heapq.heappop(max_heap)
                    ans.append(k_2)
                    v_2 += 1
                    if v_2 < 0:
                        heapq.heappush(max_heap, (v_2, k_2))
                    heapq.heappush(max_heap, (v_1, k_1))

        return "".join(ans)

    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)

        max_heap = []
        heapq.heapify(max_heap)

        for k, v in counter.items():
            heapq.heappush(max_heap, (-v, k))

        print(max_heap)

        ans = []

        while max_heap:

            buffer = []
            while max_heap and ans and max_heap[0][1] == ans[-1]:
                buffer.append(heapq.heappop(max_heap))

            if len(max_heap) == 0:
                break

            v, k = heapq.heappop(max_heap)

            ans.append(k)

            v += 1
            if v < 0:
                heapq.heappush(max_heap, (v, k))

            if buffer:
                while buffer:
                    v, k = buffer.pop()
                    heapq.heappush(max_heap, (v, k))

        if len(ans) == len(s):
            return "".join(ans)
        else:
            return ""