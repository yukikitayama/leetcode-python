"""
Complexity
- Let m be the length of nums1, and n be the length of nums2
- Constraint says that nums1.length <= nums2.length
- Time is O(n) for making a hashmap with key num2 and value the next greater element
"""


from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num2_to_next_greater = {}
        for i in range(len(nums2)):

            # If the current num2 is greater than the previously seen num2 in stack
            # it's the next greater element
            while stack and nums2[i] > stack[-1]:
                key = stack.pop()
                num2_to_next_greater[key] = nums2[i]

            stack.append(nums2[i])

        # For num2 which could not find the next greater element
        while stack:
            key = stack.pop()
            num2_to_next_greater[key] = -1

        print(f'stack: {stack}, num2_to_next_greater: {num2_to_next_greater}')

        res = []
        for i in range(len(nums1)):
            res.append(num2_to_next_greater[nums1[i]])

        return res


nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1 = [2,4]
nums2 = [1,2,3,4]
print(Solution().nextGreaterElement(nums1, nums2))
