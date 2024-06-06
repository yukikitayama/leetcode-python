"""
Anytime we have a positive net gain, we should consider taking this element because it can contribute to a positive sum and potentially increase the sum of subsequent subsequences.
"""

from typing import List
import collections
import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = collections.deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):

            # Discard if it's too far from current
            if queue and queue[0] < i - k:
                queue.popleft()

            if queue:
                dp[i] = nums[i] + dp[queue[0]]
            else:
                dp[i] = nums[i]

            # To keep monotonically descreasing
            # discard previously seen element which is smaller than current
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()

            if dp[i] > 0:
                queue.append(i)

        return max(dp)

    def constrainedSubsetSum1(self, nums: List[int], k: int) -> int:
        max_heap = []
        heapq.heappush(max_heap, (-nums[0], 0))
        ans = nums[0]

        for i in range(1, len(nums)):

            # Discard previous if it's too far from current
            while max_heap and max_heap[0][1] < i - k:
                heapq.heappop(max_heap)

            curr = nums[i] + max(
                # Discard previous
                0,
                # Or use the previous
                -max_heap[0][0]
            )

            ans = max(ans, curr)

            heapq.heappush(max_heap, (-curr, i))

        return ans