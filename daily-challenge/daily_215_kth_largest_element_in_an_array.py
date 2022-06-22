from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # If we keep min heap with size of k, the top of the heap is kth largest element
        # because the larger elements are the bottom of the heap
        heap = []
        heapq.heapify(heap)
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)

        # print(heap)

        return heap[0]


# This is not optimized, because heap becomes biggest size, but you don't need to push everything at once
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

        for i in range(k):
            popped = -1 * heapq.heappop(heap)
            if i == k - 1:
                return popped


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(Solution().findKthLargest(nums, k))
