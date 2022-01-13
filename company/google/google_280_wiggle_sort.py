"""
- sort first
- and then wiggly append to answer
"""


from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        less = True
        for i in range(len(nums) - 1):
            if less:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            less = not less

        print(nums)


class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i + 1], nums[i] = nums[i], nums[i + 1]

        print(nums)


"""
- Time is O(nlogn) because sort() takes nlogn
"""

if __name__ == '__main__':
    nums = [3, 5, 2, 1, 6, 4]
    print(Solution().wiggleSort(nums))
