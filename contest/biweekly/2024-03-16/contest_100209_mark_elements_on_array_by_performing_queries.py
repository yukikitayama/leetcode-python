from typing import List
import heapq


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        min_heap = []
        heapq.heapify(min_heap)
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i], i))

        marked = [False] * len(nums)

        ans = []
        total = sum(nums)

        for index, k in queries:

            if not marked[index]:
                total -= nums[index]
                marked[index] = True

            while min_heap and k > 0:

                num, i = heapq.heappop(min_heap)

                if not marked[i]:
                    total -= num
                    marked[i] = True
                    k -= 1

            ans.append(total)

        return ans