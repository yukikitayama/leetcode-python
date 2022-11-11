"""
- Two pointers
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        left = 0
        right = 1
        k = 1

        while right < len(nums):

            if nums[right] == nums[left]:
                right += 1
            else:
                left += 1
                k += 1
                nums[left] = nums[right]
                right += 1

        return k


if __name__ == '__main__':
    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
