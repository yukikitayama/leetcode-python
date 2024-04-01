from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_num = {i: nums[i] for i in range(len(nums)) if nums[i] != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        this_idxs = set(self.index_to_num.keys())
        that_idxs = set(vec.index_to_num.keys())
        common_idxs = this_idxs.intersection(that_idxs)

        ans = 0
        for i in common_idxs:
            ans += self.index_to_num[i] * vec.index_to_num[i]

        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)