"""
Sliding window
nums: [1, 2, 3]
bin: [01, 10, 11]
OR: [01, 11, 11]

Brute force
"""

from typing import List


class Solution:
    def minimumSubarrayLength1(self, nums: List[int], k: int) -> int:
        return 0

        left = 0
        curr = 0

        for right in range(len(nums)):
            #             curr |= nums[right]

            #             # Contract
            #             while curr >= 2**(k - 1):

            print(bin(nums[right]))

        return 0

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        ans = float("inf")

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:(j + 1)]
                curr = 0
                for s in range(len(subarray)):
                    curr |= subarray[s]

                # print(f"curr: {curr}, k: {k}, i: {i}, j: {j}, j - i + 1: {j - i + 1}")

                if curr >= k:
                    ans = min(ans, j - i + 1)

        # print()

        return -1 if ans == float("inf") else ans
