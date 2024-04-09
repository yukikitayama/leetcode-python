"""
Brute force
  2 nested loops
  when i and j are different, compute sum and update max sum so far
  T: O(N**2)

Sort and two pointers
  initialize left 0 and right length - 1
  if curr sum is bigger than k
    decrement right
  if curr sum is smaller than k
    increment left
  T: O(NlogN)
"""

from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # nums: [1, 2, 3]
        # counts: [0, 1, 1, 1]
        counts = [0] * (max(nums) + 1)
        for i in range(len(nums)):
            counts[nums[i]] += 1

        # print(counts)

        left = 1
        right = len(counts) - 1
        ans = -1

        while left <= right:
            if left + right >= k:
                right -= 1
            elif counts[right] == 0:
                right -= 1
            else:
                if (
                        (left < right and counts[left] > 0)
                        or (left == right and counts[left] > 1)
                ):
                    ans = max(ans, left + right)
                left += 1
            # print(left, right)

        return ans

    def twoSumLessThanK3(self, nums: List[int], k: int) -> int:
        ans = -1
        nums.sort()

        print(nums)

        def binary_search(i, target):
            # i < j
            left = i + 1
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                # sum < k
                if nums[mid] == target:
                    right = mid - 1

                elif nums[mid] > target:
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1
            return left

        for i in range(len(nums)):
            target = k - nums[i]
            j = binary_search(i, target) - 1
            if i < j:
                # print(f"target: {target}, i: {i}, nums[i]: {nums[i]}, j: {j}, nums[j]: {nums[j]}, sum: {nums[i] + nums[j]}")
                ans = max(ans, nums[i] + nums[j])

        return ans

    def twoSumLessThanK2(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            sum_ = nums[left] + nums[right]

            if sum_ >= k:
                right -= 1
            else:
                ans = max(ans, sum_)
                left += 1

        return ans

    def twoSumLessThanK1(self, nums: List[int], k: int) -> int:
        ans = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum_ = nums[i] + nums[j]
                if sum_ < k:
                    ans = max(ans, sum_)

        return ans
