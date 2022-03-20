from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        is_greater = False
        is_smaller = False

        for i in range(len(nums) - 1):

            if nums[i] < nums[i + 1]:
                is_greater = True

            if nums[i] > nums[i + 1]:
                is_smaller = True

            if is_greater and is_smaller:
                return False

        return True


if __name__ == '__main__':
    nums = [1,2,2,3]
    nums = [6, 5, 4, 4]
    nums = [1, 3, 2]
    print(Solution().isMonotonic(nums))