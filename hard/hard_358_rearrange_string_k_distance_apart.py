import heapq
import collections


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counter = collections.Counter([ch for ch in s])
        max_heap = []

        for ch, freq in counter.items():
            heapq.heappush(max_heap, (-freq, ch))

        queue = collections.deque()

        ans = []

        while len(ans) != len(s):

            curr_index = len(ans)

            # queue[0][0] is previous index
            if queue and curr_index - queue[0][0] >= k:
                prev_index, prev_char = queue.popleft()
                heapq.heappush(max_heap, (-counter[prev_char], prev_char))

            if not max_heap:
                return ""

            curr_count, curr_char = heapq.heappop(max_heap)

            ans.append(curr_char)

            counter[curr_char] -= 1
            if counter[curr_char] > 0:
                queue.append([curr_index, curr_char])

        return "".join(ans)