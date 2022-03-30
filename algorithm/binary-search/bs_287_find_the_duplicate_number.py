"""
- Find the first number to have its counts exceed the actual number
- Count is monotonic increase for binary search

- Find the smallest number s.t. the count of numbers less than or equal to its number
  is greater than the number itself
- Time is O(NlogN) because for each binary search (logN), linear scan to count up (N)
"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            count = sum(num <= mid for num in nums)

            if count > mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]
    print(Solution().findDuplicate(nums))
