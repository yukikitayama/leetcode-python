"""
- Finding smallest operations summing up to x is to find longest subarray summing up to total - x
  - Because longest subarray are one which are not used
"""


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        max_len = -1
        left = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr > total - x and left <= right:
                curr -= nums[left]
                left += 1

            if total - x == curr:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1


if __name__ == '__main__':
    nums = [1, 1, 4, 2, 3]
    x = 5
    # 2
    nums = [5, 6, 7, 8, 9]
    x = 4
    # -1
    nums = [3, 2, 20, 1, 1, 3]
    x = 10
    # 5
    print(Solution().minOperations(nums, x))
