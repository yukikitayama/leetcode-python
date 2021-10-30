"""
- min heap
"""


from typing import List
import itertools
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # First takes O(nlogn) to push all the items onto the heap
        # Then takes O(klogn) to find the kth smallest element
        # So time is  O(nlogn)
        return [[num1, num2] for num1, num2 in heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum)]


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 2
# nums1 = [1,2]
# nums2 = [3]
# k = 3
# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 10
print(Solution().kSmallestPairs(nums1, nums2, k))




