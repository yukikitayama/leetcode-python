"""
- brute force with TLE
"""


from typing import List
import itertools


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        cartesian = itertools.product(nums1, nums2)
        cartesian = [[num1, num2] for num1, num2 in cartesian]
        return sorted(cartesian, key=sum)[:k]


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




