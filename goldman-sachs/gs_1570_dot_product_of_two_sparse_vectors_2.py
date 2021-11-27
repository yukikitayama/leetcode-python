"""
- Use hashmap with key index and value num
  - Any index which is not in the hashmap corresponds to num 0
- Space is optimized because we only store nonzero values, and
  we can discard lots of values because input is sparse vectors.
"""


from typing import List
import collections


class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_num = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num != 0:
                self.index_to_num[i] = num

    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, num in vec.index_to_num.items():
            if i in self.index_to_num:
                ans += self.index_to_num[i] * num
        return ans

nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
# 8
nums1 = [0,1,0,0,0]
nums2 = [0,0,0,0,2]
# 0
nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]
# 6
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(f'ans: {ans}')


