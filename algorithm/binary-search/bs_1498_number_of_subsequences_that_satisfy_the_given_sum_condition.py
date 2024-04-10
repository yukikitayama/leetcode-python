"""
Sort nums
Iterate nums
  for each num as min num, binary search the max num to the right

From min num idx and max num idx, how to find the number of subsequences
  For each element after min (right - left), 2 options; we either include or exclude
  [3, 5, 6]
    [3, 5, 6]
    [3, _, 6]
    [3, 5, _]
    [3, _, _]
  left: 0, right: 2
    2**(right - left) = 2**2 = 4
"""

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0

        left = 0
        right = len(nums) - 1

        while left <= right:

            while right >= 0 and nums[right] > target - nums[left]:
                right -= 1

            if left <= right:
                # ans = (ans + 2 ** (right - left)) % (10 ** 9 + 7)
                # Using built-in pow() is faster https://docs.python.org/3/library/functions.html#pow
                ans = (ans + pow(2, right - left, (10 ** 9 + 7))) % (10 ** 9 + 7)

            left += 1

        return ans

    def numSubseq1(self, nums: List[int], target: int) -> int:

        def binary_search(left):
            diff = target - nums[left]
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                # [3, 5, 6, 7]
                # Left space could have duplicated number
                if nums[mid] == diff:
                    left = mid + 1

                elif nums[mid] < diff:
                    left = mid + 1

                elif nums[mid] > diff:
                    right = mid - 1

            return left - 1

        ans = 0

        nums.sort()

        for left in range(len(nums)):

            right = binary_search(left)

            # print(left, right)

            if left <= right:
                ans = (ans + 2 ** (right - left)) % (10 ** 9 + 7)

        return ans
