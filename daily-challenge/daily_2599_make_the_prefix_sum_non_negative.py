"""
queue, prefix sum, simulation

There may be earlier elements that are smaller (more negative) than nums[i], and moving one of those instead would result in a larger prefixSum, reducing the chances of needing further operations later.
"""

from typing import List
import heapq
import collections


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        min_heap = []
        prefix_sum = 0
        ans = 0

        for num in nums:

            if num < 0:
                heapq.heappush(min_heap, num)

            prefix_sum += num

            if prefix_sum < 0:
                negative_num = heapq.heappop(min_heap)
                prefix_sum -= negative_num
                ans += 1

        return ans

    def makePrefSumNonNegative1(self, nums: List[int]) -> int:
        queue = collections.deque(nums)
        prefix_sum = 0
        ans = 0
        while queue:
            num = queue.popleft()

            if prefix_sum + num < 0:
                queue.append(num)
                ans += 1

            else:
                prefix_sum += num

        return ans
