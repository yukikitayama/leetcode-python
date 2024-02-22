"""
Find indices where both arrays have non-zero value
Hashmap index to num
intersection of hashmap key to compute
"""

from typing import List
import collections


class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_num = collections.defaultdict(int)
        for i in range(len(nums)):
            if nums[i] > 0:
                self.index_to_num[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # indices = set(self.index_to_num.keys()).intersection(set(vec.index_to_num.keys()))
        # ans = 0
        # for i in indices:
        #     ans += self.index_to_num[i] * vec.index_to_num[i]
        # return ans

        ans = 0
        for i in self.index_to_num:
            if i in vec.index_to_num:
                ans += self.index_to_num[i] * vec.index_to_num[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)