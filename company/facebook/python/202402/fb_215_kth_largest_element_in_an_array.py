"""
Iterate nums
  Append num toMax heap
Return kth from the top of max heap

Edge
  nums length < k, nothing to return
  k = 0

T: O(nlogk)
  n iterate
  logk add element to heap, k is tree hight
S: O(n)
  heap
"""

class Solution:

    # Max heap
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     max_heap = []
    #     heapq.heapify(max_heap)

    #     for i in range(len(nums)):

    #         curr = nums[i]
    #         heapq.heappush(max_heap, -curr)

    #     i = 0
    #     ans = None
    #     while i < k:
    #         ans = -1 * heapq.heappop(max_heap)
    #         i += 1
    #     return ans

    # Min heap
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     min_heap = []
    #     heapq.heapify(min_heap)

    #     for i in range(len(nums)):
    #         curr = nums[i]
    #         heapq.heappush(min_heap, curr)
    #         if len(min_heap) > k:
    #             heapq.heappop(min_heap)

    #     # [0] return min heap top
    #     return min_heap[0]

    # Counting sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        # 5, 1, 5 - 1 + 1 = 5, to access, i - min
        # 5, -1, 5 + 1 + 1 = 7, [_, _, _, _, _, _. _]
        # We need to minus min to access
        counter = [0] * (max_num - min_num + 1)

        for num in nums:
            counter[num - min_num] += 1

        remain = k
        for i in range(len(counter) - 1, -1, -1):
           remain -= counter[i]
           if remain <= 0:
               # We need to plus min to get num
               return i + min_num
        return -1
