from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2

        # Find first decreasing element from the right
        # e.g. 1, 4, 3, 2 <= 1 is the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            # Find the small value to the right of nums[i]
            while nums[i] >= nums[j]:
                j -= 1
            self.swap(nums, i, j)

        self.reverse(nums, i + 1)
        print(nums)

    def swap(self, nums, i, j):
        # Swap the values in nums in place
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1


"""
Time complexity
Let n be the length of nums, O(n) to scan from right to left, and O(n) to scan from left to right
so O(n + n) = O(2n) = O(n)

Space comlexity
O(1) because it does it in place
"""


# nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
nums = [1,2,3]
# nums = [3,2,1]
# nums = [1,1,5]
# nums = [1]
print(Solution().nextPermutation(nums))
