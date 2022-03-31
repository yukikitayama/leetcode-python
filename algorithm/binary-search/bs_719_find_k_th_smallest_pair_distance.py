"""
- Binary search with search space of the absolute difference
  left is 0 and right is (max(nums) - min(nums))
"""


from typing import List
import heapq


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def possible(distance):
            count = 0
            left_idx = 0
            for right_idx, right_num in enumerate(nums):

                # Sliding window
                # End condition: current distance is smaller than the given distance
                # We wanna count the pairs of (nums[right] - nums[left] <= distance)
                while right_num - nums[left_idx] > distance:
                    left_idx += 1

                # Number of pairs with right as rightmost is (right - left)
                count += (right_idx - left_idx)

                # print(f'  left_idx: {left_idx}, right_idx: {right_idx}, count: {count}')

            # print(f'    count: {count}')

            return count >= k

        nums.sort()

        left = 0
        # Max - min
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            # print(f'left: {left}, mid: {mid}, right: {right}')

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left


class Solution1:
    """
    Time is O((K + N)logN) because sort takes O(NlogN) and finding kth smallest from heap takes O(KlogN)
    """
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Time O(NlogN)
        nums.sort()

        # Heap: [(distance, root index, neighbor index), ...]
        # Root index is fixed, and neighbor index is expanded
        # -1 in range because +1 index to be in bound
        # Find kth smallest, so min heap
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
        # Time O(N)
        heapq.heapify(heap)

        # Find kth smallest
        # Time O(K)
        for _ in range(k):
            # Time O(logN)
            distance, root, neighbor = heapq.heappop(heap)

            # Create a next pair and push it to heap if index in the boundary
            if neighbor + 1 < n:
                heapq.heappush(heap, (nums[neighbor + 1] - nums[root], root, neighbor + 1))

        return distance


if __name__ == '__main__':
    nums = [1, 3, 1]
    k = 1
    print(Solution().smallestDistancePair(nums, k))

