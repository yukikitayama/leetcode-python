"""
- better brute force by starting index in nums2 from the current num in nums1
"""


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_to_index = {}
        for i in range(len(nums2)):
            num2_to_index[nums2[i]] = i

        res = []

        for i in range(len(nums1)):

            print(f'i: {i}')

            for j in range(num2_to_index[nums1[i]] + 1, len(nums2)):

                print(f'  j: {j}')

                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break

            if j == len(nums2) - 1 or num2_to_index[nums1[i]] == len(nums2) - 1:
                res.append(-1)

        return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]
print(Solution().nextGreaterElement(nums1, nums2))
