from typing import List
import heapq
import collections


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        id_to_freq = collections.Counter()

        ans = []

        for i in range(len(nums)):

            n = nums[i]
            f = freq[i]

            if n not in id_to_freq:

                heapq.heappush(max_heap, (-f, n))

                id_to_freq[n] += f

            else:
                buffer = []
                while max_heap[0][1] != n:
                    buffer.append(heapq.heappop(max_heap))
                p_f, p_n = heapq.heappop(max_heap)
                p_f -= f
                heapq.heappush(max_heap, (p_f, p_n))
                while buffer:
                    heapq.heappush(max_heap, buffer.pop())

            # print(i, max_heap)

            ans.append(max_heap[0][0] * -1)

        return ans

    def mostFrequentIDs1(self, nums: List[int], freq: List[int]) -> List[int]:
        id_to_freq = collections.Counter()

        ans = []

        for i in range(len(nums)):
            id_to_freq[nums[i]] += freq[i]

            most_frequent = max(id_to_freq.values())
            ans.append(most_frequent)

        return ans