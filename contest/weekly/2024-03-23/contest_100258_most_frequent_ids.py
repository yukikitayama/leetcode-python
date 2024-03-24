from typing import List
import heapq
import collections


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        id_to_freq = collections.Counter()

        ans = [0] * len(nums)

        for i in range(len(nums)):

            n = nums[i]
            f = freq[i]

            id_to_freq[n] += f

            # This make heap contains duplicated IDs with different freq
            # but it's okay because we only care heap top freq and ID
            heapq.heappush(max_heap, (-id_to_freq[n], n))

            # This pops outdate large freq and ID
            # e.g. previously freq was 2, but currently freq is 0, 2 at the heap top, so discard it
            while max_heap and -max_heap[0][0] != id_to_freq[max_heap[0][1]]:
                heapq.heappop(max_heap)

            if max_heap:
                ans[i] = -max_heap[0][0]

            # print(i, max_heap)

        return ans

    def mostFrequentIDs1(self, nums: List[int], freq: List[int]) -> List[int]:
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