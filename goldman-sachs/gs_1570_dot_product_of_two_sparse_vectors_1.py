"""
Result
- Start: 8:55
- End: 9:02
- Solved: 1
- Optimized: 0
- Saw solution: 0
- Time is O(n)
- Space is O(n)

"""


from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for num1, num2 in zip(self.nums, vec.nums):
            ans += num1 * num2
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


