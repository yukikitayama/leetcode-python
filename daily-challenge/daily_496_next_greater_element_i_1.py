"""
- brute force
"""


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):

                if found and nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break

                if nums2[j] == nums1[i]:
                    found = True

                if j == len(nums2) - 1 and found:
                    res.append(-1)

        return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]
print(Solution().nextGreaterElement(nums1, nums2))
