"""
We first observe that the range of possible distances is finite and bounded:
The minimum distance is 0, occurring when two numbers in the array are identical.
The maximum distance is the difference between the largest and smallest numbers in the array.

This bounded range allows us to use binary search to efficiently find the k-th smallest distance.

The efficiency of this approach is due to the combination of binary search, which reduces the search space logarithmically, and the sliding window technique, which allows us to count pairs in linear time for each binary search iteration, given that the array is sorted.
"""

from typing import List
import heapq


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def count_pairs_with_max_distance(m):
            count = 0
            left = 0
            for right in range(len(nums)):

                # Invalid case
                while nums[right] - nums[left] > m:
                    left += 1

                # Here distance <= m, so we can count valid pairs
                count += right - left

            return count

        nums.sort()
        low = 0
        high = max(nums) - min(nums)
        ans = None

        while low <= high:

            mid = (low + high) // 2

            count = count_pairs_with_max_distance(mid)

            if count == k:
                ans = mid
                high = mid - 1
            elif count < k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans

    def smallestDistancePair1(self, nums: List[int], k: int) -> int:
        max_num = max(nums)

        distance_bucket = [0] * (max_num + 1)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d = abs(nums[i] - nums[j])

                distance_bucket[d] += 1

        for d in range(len(distance_bucket)):
            k -= distance_bucket[d]
            if k <= 0:
                return d

        # return -1

    def smallestDistancePair1(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d = abs(nums[i] - nums[j])
                heapq.heappush(max_heap, -d)
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        return -max_heap[0]