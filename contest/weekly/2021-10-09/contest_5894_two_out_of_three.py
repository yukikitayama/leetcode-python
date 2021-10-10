"""
- make sets for each nums
- intersect nums1 and nums2
- intersect nums2 and nums3
- intersect nums3 and nums1
- set of all the intersections
"""


from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        intersect_1_2 = set(nums1).intersection(set(nums2))
        intersect_2_3 = set(nums2).intersection(set(nums3))
        intersect_3_1 = set(nums3).intersection(set(nums1))

        all = intersect_1_2.union(intersect_2_3).union(intersect_3_1)
        return list(all)


nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
print(Solution().twoOutOfThree(nums1, nums2, nums3))
