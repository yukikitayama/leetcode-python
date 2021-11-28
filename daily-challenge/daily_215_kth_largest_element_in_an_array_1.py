from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Returns a list with length k in a descending order
        return heapq.nlargest(k, nums)[-1]


"""
Time complexity
Let k the size of the binary tree, n be the length of nums
O(nlogk) because adding element to heap is O(logk) and we do n times to iterate nums

Space complexity
O(k) to store heap
"""


nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))
