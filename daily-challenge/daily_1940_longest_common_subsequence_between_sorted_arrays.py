"""
Heap
  [(val, arrays index, each array index)]
"""

from typing import List
import collections


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        """Two pointers"""

        def find_lcs(nums1, nums2):
            res = []
            p1 = p2 = 0

            while p1 < len(nums1) and p2 < len(nums2):

                if nums1[p1] < nums2[p2]:
                    p1 += 1

                elif nums1[p1] > nums2[p2]:
                    p2 += 1

                else:
                    res.append(nums1[p1])
                    p1 += 1
                    p2 += 1

            return res

        curr_lcs = arrays[0]

        for array in arrays[1:]:
            curr_lcs = find_lcs(
                curr_lcs,
                array
            )

        return curr_lcs

    def longestCommonSubsequence1(self, arrays: List[List[int]]) -> List[int]:
        """Hashmap"""
        counter = collections.Counter()

        ans = []

        for array in arrays:

            for num in array:

                counter[num] += 1

                # This only works for the last array
                if counter[num] == len(arrays):
                    # for num in array is guaranteed to be sorted order,
                    # so appending is also sorted
                    ans.append(num)

        return ans
