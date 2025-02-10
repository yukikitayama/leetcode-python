"""
nums[i] + nums[j] + complement = 0
complement = -nums[i] - nums[j]
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def check(left):
            right = left + 1
            seen = set()
            while right < len(nums):
                complement = -nums[left] - nums[right]
                if complement in seen:
                    ans.append([nums[left], complement, nums[right]])

                    while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                        right += 1

                seen.add(nums[right])
                right += 1

        nums.sort()
        for i in range(len(nums)):

            # If current is positive, the remaining sum cannot form negative
            if nums[i] > 0:
                break

            if i == 0:
                check(i)

            # Exclude duplicate triplets
            elif nums[i - 1] != nums[i]:
                check(i)

        return ans

    def threeSum1(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def check(left):
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                sum_ = nums[left] + nums[mid] + nums[right]
                if sum_ == 0:
                    ans.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    # No duplicates
                    # If this is false and nums[right] == nums[right + 1]
                    # [0, 1, 3], [0, 2, 3], these are still distinct
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                elif sum_ < 0:
                    mid += 1
                elif sum_ > 0:
                    right -= 1

        nums.sort()
        for i in range(len(nums)):

            # If current is positive, the remaining sum cannot form negative
            if nums[i] > 0:
                break

            if i == 0:
                check(i)

            # Exclude duplicate triplets
            elif nums[i - 1] != nums[i]:
                check(i)

        return ans