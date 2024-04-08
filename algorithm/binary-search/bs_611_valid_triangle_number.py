"""
Triangle
  sum of 2 sides > one side

Sort array
three pointers?

when a <= b <= c
  when a + b > c
    b + c > a is true because a <= c
    c + a > b is true because b <= c
"""

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        ans = 0

        nums.sort()

        for i in range(len(nums) - 2):
            k = i + 2

            # Edge case
            if nums[i] == 0:
                continue

            for j in range(i + 1, len(nums) - 1):
                # if nums[j] == 0:
                #     break

                # Find first invalid k
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1

                # print(i, j, k, (k - 1) - (j + 1) + 1)

                # 1, 2, 4
                # (4 - 1) - (2 + 1) + 1 = 3 - 3 + 1
                ans += (k - 1) - (j + 1) + 1

        return ans

    def triangleNumber2(self, nums: List[int]) -> int:

        def binary_search(left, target):
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # a + b > c, but we need to find invalid c
                if nums[mid] < target:
                    # Go to right to have bigger c to have invalid triangle
                    left = mid + 1

                # Invalid, but we might have leftmost invalid
                elif nums[mid] > target:
                    right = mid - 1

                elif nums[mid] == target:
                    right = mid - 1

            return left

        nums.sort()
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # k is leftmost invalid index
                k = binary_search(j + 1, nums[i] + nums[j])

                # Valid number of triplets
                # k-1: index upto valid
                # j+1: index starting cout
                # +1: be inclusive
                num_valid = (k - 1) - (j + 1) + 1

                ans += num_valid

        return ans

    def triangleNumber1(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (
                            nums[i] + nums[j] > nums[k]
                            and nums[j] + nums[k] > nums[i]
                            and nums[k] + nums[i] > nums[j]
                    ):
                        ans += 1

        return ans
